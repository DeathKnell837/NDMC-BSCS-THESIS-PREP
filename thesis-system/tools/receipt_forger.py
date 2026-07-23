"""
Receipt Forgery Editor — ForgeGuard Thesis Tool
=================================================
Takes REAL GCash/Maya receipt screenshots and applies forgery
techniques to create forged versions for CNN training.

Forgery Types:
  1. Amount alteration — paints over the amount, writes a different value
  2. Reference number fabrication — replaces ref number with fake digits
  3. Name modification — changes the recipient/sender name

The tool detects text regions based on the standard GCash/Maya layout,
paints over them, and redraws with new values. The subtle pixel artifacts
(font mismatch, color bleeding, anti-aliasing differences) are what the
CNN learns to detect.

Usage:
  python receipt_forger.py --input ./authentic/ --output ./forged/ --type amount
  python receipt_forger.py --input ./authentic/ --output ./forged/ --type all
  python receipt_forger.py --input photo.png --output ./forged/ --type name --difficulty hard

Difficulty Levels:
  easy   — obvious font/color mismatch (30% of forgeries)
  medium — correct font but subtle pixel artifacts (40%)
  hard   — near-identical, minimal visible difference (30%)
"""

import os
import sys
import random
import string
import argparse
import json
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import colorsys

# ============================================================
# CONFIGURATION
# ============================================================

# Windows font paths
FONTS_DIR = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')

# GCash receipt field regions (approximate Y-ranges for 1080x1920 screenshots)
# These may need adjustment based on the actual phone model
GCASH_REGIONS = {
    'amount': {
        'y_start': 380,    # Top of amount text area
        'y_end': 470,      # Bottom of amount text area
        'x_start': 100,    # Left boundary
        'x_end': 980,      # Right boundary
        'font_size': 80,
        'font_color': (0, 100, 210),  # GCash blue
        'align': 'center',
    },
    'name': {
        'y_start': 505,    # "Sent to" value row
        'y_end': 560,
        'x_start': 450,
        'x_end': 940,
        'font_size': 38,
        'font_color': (30, 30, 30),
        'align': 'right',
    },
    'ref_number': {
        'y_start': 640,    # "Ref. No." value row
        'y_end': 695,
        'x_start': 450,
        'x_end': 940,
        'font_size': 38,
        'font_color': (30, 30, 30),
        'align': 'right',
    },
}

# Maya receipt field regions (approximate — green-themed UI)
MAYA_REGIONS = {
    'amount': {
        'y_start': 400,
        'y_end': 490,
        'x_start': 100,
        'x_end': 980,
        'font_size': 80,
        'font_color': (0, 160, 100),  # Maya green
        'align': 'center',
    },
    'name': {
        'y_start': 530,
        'y_end': 585,
        'x_start': 450,
        'x_end': 940,
        'font_size': 38,
        'font_color': (30, 30, 30),
        'align': 'right',
    },
    'ref_number': {
        'y_start': 660,
        'y_end': 715,
        'x_start': 450,
        'x_end': 940,
        'font_size': 38,
        'font_color': (30, 30, 30),
        'align': 'right',
    },
}

# Filipino name pools for replacement
FILIPINO_FIRST_NAMES = [
    "Maria", "Jose", "Juan", "Ana", "Mark", "John", "Jay", "Kim",
    "Angel", "Mae", "Rose", "Grace", "Carl", "Ryan", "Paolo",
    "Trisha", "Kevin", "Jan", "Nicole", "Patrick", "Althea",
    "Daniela", "Rogie", "Christian", "Jhon", "Kyla", "Joshua",
    "Ericka", "Renz", "Precious", "Diana", "Miguel", "Sofia",
    "Chloe", "Lance", "Bea", "Marco", "Ella", "Jerome", "Alyssa",
    "Kenneth", "Jasmine", "Ralph", "Czarina", "Vince", "Cherry",
]

FILIPINO_LAST_NAMES = [
    "Santos", "Reyes", "Cruz", "Bautista", "Garcia", "Mendoza",
    "Torres", "Villanueva", "Gonzales", "Lopez", "Aquino", "Ramos",
    "Castillo", "Rivera", "Fernandez", "Diaz", "Morales", "Soriano",
    "Navarro", "Flores", "Dela Cruz", "De Leon", "Delos Santos",
    "Manalo", "Pascual", "Salazar", "Aguilar", "Mercado", "Bondad",
]

COMMON_AMOUNTS = [
    50, 100, 150, 200, 250, 300, 350, 400, 450, 500,
    600, 700, 750, 800, 900, 1000, 1200, 1500, 1800,
    2000, 2500, 3000, 3500, 4000, 4500, 5000,
    6000, 7000, 7500, 8000, 9000, 10000, 15000, 20000,
]


# ============================================================
# FONT UTILITIES
# ============================================================

def get_font(name, size):
    """Load a system font with fallback."""
    font_map = {
        'bold': 'arialbd.ttf',
        'regular': 'arial.ttf',
        'italic': 'ariali.ttf',
        'segoe': 'segoeui.ttf',
        'segoe_bold': 'segoeuib.ttf',
        'segoe_light': 'segoeuil.ttf',
        'calibri': 'calibri.ttf',
        'calibri_bold': 'calibrib.ttf',
        'tahoma': 'tahoma.ttf',
        'verdana': 'verdana.ttf',
    }
    try:
        path = os.path.join(FONTS_DIR, font_map.get(name, 'arial.ttf'))
        return ImageFont.truetype(path, size)
    except (OSError, IOError):
        return ImageFont.load_default()


# ============================================================
# FORGERY DIFFICULTY SETTINGS
# ============================================================

def get_difficulty_params(difficulty):
    """
    Return forgery parameters based on difficulty level.
    
    Easy:   Obvious mismatches — wrong font, wrong color, wrong size
    Medium: Correct font family but subtle artifacts — slight color shift,
            minor size difference, faint background mismatch
    Hard:   Near-identical — same font, same color, minimal artifacts
            (only detectable by ELA/pixel-level analysis)
    """
    if difficulty == 'easy':
        return {
            # Use a clearly different font
            'font_options': ['calibri_bold', 'tahoma', 'verdana'],
            'font_size_offset': random.choice([-6, -4, 4, 6, 8]),
            # Noticeable color mismatch
            'color_offset': (
                random.randint(-30, 30),
                random.randint(-30, 30),
                random.randint(-30, 30),
            ),
            # Obvious position shift
            'position_offset': (random.randint(-5, 5), random.randint(-4, 4)),
            # Visible background patch mismatch
            'bg_blend_quality': 'low',
            # Add slight blur to the edited region (sloppy edit)
            'apply_blur': random.random() > 0.5,
            'blur_radius': random.uniform(0.8, 1.5),
        }
    elif difficulty == 'medium':
        return {
            # Similar font family but not exact
            'font_options': ['segoe_bold', 'bold', 'calibri_bold'],
            'font_size_offset': random.choice([-2, -1, 1, 2]),
            # Subtle color shift
            'color_offset': (
                random.randint(-10, 10),
                random.randint(-10, 10),
                random.randint(-10, 10),
            ),
            # Minor position shift
            'position_offset': (random.randint(-2, 2), random.randint(-1, 1)),
            # Decent background match
            'bg_blend_quality': 'medium',
            'apply_blur': random.random() > 0.7,
            'blur_radius': random.uniform(0.3, 0.7),
        }
    else:  # hard
        return {
            # Same font family
            'font_options': ['segoe_bold'],
            'font_size_offset': 0,
            # Minimal color shift (nearly invisible to eye)
            'color_offset': (
                random.randint(-3, 3),
                random.randint(-3, 3),
                random.randint(-3, 3),
            ),
            # No position shift
            'position_offset': (0, 0),
            # High-quality background match
            'bg_blend_quality': 'high',
            'apply_blur': False,
            'blur_radius': 0,
        }


# ============================================================
# BACKGROUND SAMPLING
# ============================================================

def sample_background_color(img, region, quality='high'):
    """
    Sample the background color from the area around the text region.
    This is used to paint over the original text before writing new text.
    
    Higher quality = better color match = harder to detect forgery.
    """
    x1, y1, x2, y2 = region['x_start'], region['y_start'], region['x_end'], region['y_end']
    
    # Sample pixels from the edges of the region (where background is visible)
    pixels = []
    for x in range(x1, x2, 10):
        # Top edge (just above text)
        if y1 - 5 >= 0:
            pixels.append(img.getpixel((x, y1 - 5)))
        # Bottom edge (just below text)
        if y2 + 5 < img.height:
            pixels.append(img.getpixel((x, y2 + 5)))
    
    if not pixels:
        return (255, 255, 255)  # Default white
    
    # Average the sampled pixels
    avg_r = sum(p[0] for p in pixels) // len(pixels)
    avg_g = sum(p[1] for p in pixels) // len(pixels)
    avg_b = sum(p[2] for p in pixels) // len(pixels)
    
    if quality == 'low':
        # Add noticeable color noise (makes the patch obvious)
        avg_r = min(255, max(0, avg_r + random.randint(-15, 15)))
        avg_g = min(255, max(0, avg_g + random.randint(-15, 15)))
        avg_b = min(255, max(0, avg_b + random.randint(-15, 15)))
    elif quality == 'medium':
        # Add slight color noise
        avg_r = min(255, max(0, avg_r + random.randint(-5, 5)))
        avg_g = min(255, max(0, avg_g + random.randint(-5, 5)))
        avg_b = min(255, max(0, avg_b + random.randint(-5, 5)))
    # 'high' quality = exact color match, no noise
    
    return (avg_r, avg_g, avg_b)


# ============================================================
# CORE FORGERY FUNCTIONS
# ============================================================

def forge_amount(img, region, difficulty='medium'):
    """
    Forgery Type 1: Amount Alteration
    Paints over the original amount and writes a different value.
    """
    params = get_difficulty_params(difficulty)
    draw = ImageDraw.Draw(img)
    
    # Sample and paint background
    bg_color = sample_background_color(img, region, params['bg_blend_quality'])
    draw.rectangle(
        [region['x_start'], region['y_start'], region['x_end'], region['y_end']],
        fill=bg_color
    )
    
    # Generate a new fake amount
    new_amount = random.choice(COMMON_AMOUNTS)
    if new_amount == int(new_amount):
        amount_str = f"P{int(new_amount):,}.00"
    else:
        amount_str = f"P{new_amount:,.2f}"
    
    # Select font based on difficulty
    font_name = random.choice(params['font_options'])
    font_size = region['font_size'] + params['font_size_offset']
    font = get_font(font_name, font_size)
    
    # Calculate text color (original + offset)
    orig_color = region['font_color']
    offset = params['color_offset']
    text_color = tuple(
        min(255, max(0, orig_color[i] + offset[i])) for i in range(3)
    )
    
    # Calculate position
    bbox = draw.textbbox((0, 0), amount_str, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    if region['align'] == 'center':
        x = region['x_start'] + (region['x_end'] - region['x_start'] - text_w) // 2
    else:
        x = region['x_end'] - text_w
    
    y = region['y_start'] + (region['y_end'] - region['y_start'] - text_h) // 2
    
    # Apply position offset
    x += params['position_offset'][0]
    y += params['position_offset'][1]
    
    # Draw the forged text
    draw.text((x, y), amount_str, fill=text_color, font=font)
    
    # Optionally apply blur to edited region
    if params['apply_blur']:
        region_crop = img.crop((
            region['x_start'], region['y_start'],
            region['x_end'], region['y_end']
        ))
        region_crop = region_crop.filter(
            ImageFilter.GaussianBlur(radius=params['blur_radius'])
        )
        img.paste(region_crop, (region['x_start'], region['y_start']))
    
    return img, {'forgery_type': 'amount_alteration', 'new_value': amount_str,
                 'difficulty': difficulty}


def forge_ref_number(img, region, difficulty='medium'):
    """
    Forgery Type 2: Reference Number Fabrication
    Replaces the reference number with random digits.
    """
    params = get_difficulty_params(difficulty)
    draw = ImageDraw.Draw(img)
    
    # Sample and paint background
    bg_color = sample_background_color(img, region, params['bg_blend_quality'])
    draw.rectangle(
        [region['x_start'], region['y_start'], region['x_end'], region['y_end']],
        fill=bg_color
    )
    
    # Generate fake reference number (13 digits like GCash)
    fake_ref = ''.join([str(random.randint(0, 9)) for _ in range(13)])
    
    # Select font based on difficulty
    font_name = random.choice(params['font_options'])
    font_size = region['font_size'] + params['font_size_offset']
    font = get_font(font_name, font_size)
    
    # Text color with offset
    orig_color = region['font_color']
    offset = params['color_offset']
    text_color = tuple(
        min(255, max(0, orig_color[i] + offset[i])) for i in range(3)
    )
    
    # Position (right-aligned)
    bbox = draw.textbbox((0, 0), fake_ref, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = region['x_end'] - text_w + params['position_offset'][0]
    y = region['y_start'] + (region['y_end'] - region['y_start'] - text_h) // 2
    y += params['position_offset'][1]
    
    draw.text((x, y), fake_ref, fill=text_color, font=font)
    
    if params['apply_blur']:
        region_crop = img.crop((
            region['x_start'], region['y_start'],
            region['x_end'], region['y_end']
        ))
        region_crop = region_crop.filter(
            ImageFilter.GaussianBlur(radius=params['blur_radius'])
        )
        img.paste(region_crop, (region['x_start'], region['y_start']))
    
    return img, {'forgery_type': 'ref_fabrication', 'new_value': fake_ref,
                 'difficulty': difficulty}


def forge_name(img, region, difficulty='medium'):
    """
    Forgery Type 3: Recipient/Sender Name Modification
    Changes the name to a different Filipino name.
    """
    params = get_difficulty_params(difficulty)
    draw = ImageDraw.Draw(img)
    
    # Sample and paint background
    bg_color = sample_background_color(img, region, params['bg_blend_quality'])
    draw.rectangle(
        [region['x_start'], region['y_start'], region['x_end'], region['y_end']],
        fill=bg_color
    )
    
    # Generate fake name
    first = random.choice(FILIPINO_FIRST_NAMES)
    last = random.choice(FILIPINO_LAST_NAMES)
    if random.random() > 0.5:
        middle = random.choice(string.ascii_uppercase)
        fake_name = f"{first} {middle}. {last}"
    else:
        fake_name = f"{first} {last}"
    
    # Select font based on difficulty
    font_name = random.choice(params['font_options'])
    font_size = region['font_size'] + params['font_size_offset']
    font = get_font(font_name, font_size)
    
    # Text color with offset
    orig_color = region['font_color']
    offset = params['color_offset']
    text_color = tuple(
        min(255, max(0, orig_color[i] + offset[i])) for i in range(3)
    )
    
    # Position (right-aligned)
    bbox = draw.textbbox((0, 0), fake_name, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = region['x_end'] - text_w + params['position_offset'][0]
    y = region['y_start'] + (region['y_end'] - region['y_start'] - text_h) // 2
    y += params['position_offset'][1]
    
    draw.text((x, y), fake_name, fill=text_color, font=font)
    
    if params['apply_blur']:
        region_crop = img.crop((
            region['x_start'], region['y_start'],
            region['x_end'], region['y_end']
        ))
        region_crop = region_crop.filter(
            ImageFilter.GaussianBlur(radius=params['blur_radius'])
        )
        img.paste(region_crop, (region['x_start'], region['y_start']))
    
    return img, {'forgery_type': 'name_modification', 'new_value': fake_name,
                 'difficulty': difficulty}


# ============================================================
# REGION CALIBRATION TOOL
# ============================================================

def calibrate_regions(image_path):
    """
    Interactive tool to help the user define text field regions
    for their specific phone model.
    
    Opens the image and lets the user verify/adjust the default regions.
    Saves calibration to a JSON file for reuse.
    """
    img = Image.open(image_path)
    w, h = img.size
    
    print(f"\nImage size: {w}x{h}")
    print(f"Default regions are calibrated for 1080x1920.")
    
    if w != 1080 or h != 1920:
        # Scale regions proportionally
        scale_x = w / 1080
        scale_y = h / 1920
        print(f"Scaling regions by {scale_x:.2f}x (horizontal) and {scale_y:.2f}x (vertical)")
        
        scaled_regions = {}
        for field, region in GCASH_REGIONS.items():
            scaled_regions[field] = {
                'y_start': int(region['y_start'] * scale_y),
                'y_end': int(region['y_end'] * scale_y),
                'x_start': int(region['x_start'] * scale_x),
                'x_end': int(region['x_end'] * scale_x),
                'font_size': int(region['font_size'] * min(scale_x, scale_y)),
                'font_color': region['font_color'],
                'align': region['align'],
            }
        return scaled_regions
    
    return GCASH_REGIONS.copy()


def draw_region_overlay(image_path, regions, output_path=None):
    """
    Draw colored rectangles over the detected regions so the user
    can visually verify they're in the right place.
    """
    img = Image.open(image_path).copy()
    draw = ImageDraw.Draw(img, 'RGBA')
    
    colors = {
        'amount': (255, 0, 0, 80),       # Red overlay
        'name': (0, 255, 0, 80),          # Green overlay
        'ref_number': (0, 0, 255, 80),    # Blue overlay
    }
    
    font = get_font('bold', 28)
    
    for field, region in regions.items():
        color = colors.get(field, (255, 255, 0, 80))
        draw.rectangle(
            [region['x_start'], region['y_start'], region['x_end'], region['y_end']],
            fill=color, outline=color[:3] + (200,), width=3
        )
        # Label
        draw.text(
            (region['x_start'] + 5, region['y_start'] + 5),
            field.upper(), fill=color[:3] + (255,), font=font
        )
    
    if output_path:
        img.save(output_path)
        print(f"Region overlay saved: {output_path}")
    
    return img


# ============================================================
# BATCH PROCESSING
# ============================================================

def process_single_image(image_path, output_dir, forgery_type, difficulty,
                         regions=None, platform='gcash'):
    """
    Apply a single forgery to a single image.
    
    Args:
        image_path: path to authentic receipt screenshot
        output_dir: directory to save forged output
        forgery_type: 'amount', 'ref_number', 'name', or 'all'
        difficulty: 'easy', 'medium', or 'hard'
        regions: custom region definitions (or None for defaults)
        platform: 'gcash' or 'maya'
    
    Returns:
        list of (output_path, metadata) tuples
    """
    img = Image.open(image_path).convert('RGB')
    
    if regions is None:
        regions = calibrate_regions(image_path)
    
    results = []
    basename = os.path.splitext(os.path.basename(image_path))[0]
    
    types_to_process = ['amount', 'ref_number', 'name'] if forgery_type == 'all' else [forgery_type]
    
    for ft in types_to_process:
        # Work on a fresh copy for each forgery type
        img_copy = img.copy()
        
        if ft not in regions:
            print(f"  Warning: No region defined for '{ft}', skipping")
            continue
        
        region = regions[ft]
        
        if ft == 'amount':
            forged_img, meta = forge_amount(img_copy, region, difficulty)
        elif ft == 'ref_number':
            forged_img, meta = forge_ref_number(img_copy, region, difficulty)
        elif ft == 'name':
            forged_img, meta = forge_name(img_copy, region, difficulty)
        else:
            print(f"  Unknown forgery type: {ft}")
            continue
        
        # Build output filename
        type_dir = {
            'amount': 'amount_alteration',
            'ref_number': 'ref_fabrication',
            'name': 'name_modification',
        }[ft]
        
        out_subdir = os.path.join(output_dir, type_dir)
        os.makedirs(out_subdir, exist_ok=True)
        
        out_fname = f"{basename}_forged_{type_dir}_{difficulty}.png"
        out_path = os.path.join(out_subdir, out_fname)
        forged_img.save(out_path, 'PNG')
        
        meta['source_image'] = os.path.basename(image_path)
        meta['output_path'] = out_path
        results.append((out_path, meta))
    
    return results


def batch_forge(input_dir, output_dir, forgery_type='all',
                difficulty_distribution=None, platform='gcash', seed=42):
    """
    Process all authentic receipt images in a directory.
    
    Creates forged versions at the specified difficulty distribution.
    Default distribution: 30% easy, 40% medium, 30% hard.
    
    Args:
        input_dir: directory containing authentic receipt screenshots
        output_dir: directory for forged outputs
        forgery_type: 'amount', 'ref_number', 'name', or 'all'
        difficulty_distribution: dict like {'easy': 0.3, 'medium': 0.4, 'hard': 0.3}
        platform: 'gcash' or 'maya'
        seed: random seed for reproducibility
    """
    random.seed(seed)
    
    if difficulty_distribution is None:
        difficulty_distribution = {'easy': 0.3, 'medium': 0.4, 'hard': 0.3}
    
    # Find all images
    valid_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.webp'}
    image_files = []
    for f in sorted(os.listdir(input_dir)):
        if os.path.splitext(f)[1].lower() in valid_extensions:
            image_files.append(os.path.join(input_dir, f))
    
    if not image_files:
        print(f"No images found in {input_dir}")
        return
    
    print(f"Found {len(image_files)} authentic images in {input_dir}")
    print(f"Forgery type: {forgery_type}")
    print(f"Difficulty distribution: {difficulty_distribution}")
    print(f"Platform: {platform}")
    print(f"Output: {output_dir}")
    print("=" * 50)
    
    # Calibrate regions using the first image
    print(f"\nCalibrating regions from: {os.path.basename(image_files[0])}")
    regions = calibrate_regions(image_files[0])
    
    # Generate calibration overlay for verification
    overlay_path = os.path.join(output_dir, '_region_overlay.png')
    os.makedirs(output_dir, exist_ok=True)
    draw_region_overlay(image_files[0], regions, overlay_path)
    
    all_metadata = []
    total_forged = 0
    
    for idx, img_path in enumerate(image_files):
        # Assign difficulty based on distribution
        rand_val = random.random()
        cumulative = 0
        difficulty = 'medium'  # default
        for diff, prob in difficulty_distribution.items():
            cumulative += prob
            if rand_val <= cumulative:
                difficulty = diff
                break
        
        results = process_single_image(
            img_path, output_dir, forgery_type, difficulty,
            regions=regions, platform=platform
        )
        
        for path, meta in results:
            all_metadata.append(meta)
            total_forged += 1
        
        if (idx + 1) % 10 == 0 or idx == len(image_files) - 1:
            print(f"  Processed {idx + 1}/{len(image_files)} images "
                  f"({total_forged} forgeries created)")
    
    # Save metadata
    meta_path = os.path.join(output_dir, 'forgery_metadata.json')
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump({
            'total_forged': total_forged,
            'total_source_images': len(image_files),
            'forgery_type': forgery_type,
            'platform': platform,
            'difficulty_distribution': difficulty_distribution,
            'generated_at': datetime.now().isoformat(),
            'forgeries': all_metadata,
        }, f, indent=2, ensure_ascii=False, default=str)
    
    print(f"\n{'=' * 50}")
    print(f"Forgery generation complete!")
    print(f"  Source images:  {len(image_files)}")
    print(f"  Forgeries made: {total_forged}")
    print(f"  Metadata:       {meta_path}")
    print(f"  Region overlay: {overlay_path}")
    print(f"{'=' * 50}")


# ============================================================
# MAIN CLI
# ============================================================

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='ForgeGuard — Receipt Forgery Editor for CNN Training',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Forge all types on a single image:
  python receipt_forger.py --input receipt.png --output ./forged/ --type all

  # Batch process a directory of authentic receipts:
  python receipt_forger.py --input ./authentic/ --output ./forged/ --type all

  # Only create amount forgeries at hard difficulty:
  python receipt_forger.py --input ./authentic/ --output ./forged/ --type amount --difficulty hard

  # Calibrate: show region overlay on an image to verify positions:
  python receipt_forger.py --input receipt.png --calibrate

  # Use Maya receipt layout:
  python receipt_forger.py --input ./authentic/ --output ./forged/ --type all --platform maya
        """
    )
    parser.add_argument('--input', type=str, required=True,
                       help='Input image or directory of authentic receipts')
    parser.add_argument('--output', type=str, default='./forged',
                       help='Output directory for forged images (default: ./forged)')
    parser.add_argument('--type', type=str, default='all',
                       choices=['amount', 'ref_number', 'name', 'all'],
                       help='Type of forgery to apply (default: all)')
    parser.add_argument('--difficulty', type=str, default=None,
                       choices=['easy', 'medium', 'hard'],
                       help='Fixed difficulty level (default: mixed 30/40/30)')
    parser.add_argument('--platform', type=str, default='gcash',
                       choices=['gcash', 'maya'],
                       help='E-wallet platform layout (default: gcash)')
    parser.add_argument('--calibrate', action='store_true',
                       help='Show region overlay for calibration (no forgery)')
    parser.add_argument('--seed', type=int, default=42,
                       help='Random seed for reproducibility (default: 42)')
    
    args = parser.parse_args()
    
    if args.calibrate:
        # Calibration mode: just show the region overlay
        if os.path.isfile(args.input):
            regions = calibrate_regions(args.input)
            overlay = draw_region_overlay(args.input, regions,
                                          args.input.replace('.', '_regions.'))
            print("Calibration overlay generated. Check the image to verify regions.")
        else:
            print("Error: --calibrate requires a single image file as --input")
        sys.exit(0)
    
    if os.path.isfile(args.input):
        # Single image mode
        if args.difficulty:
            difficulty = args.difficulty
        else:
            difficulty = random.choice(['easy', 'medium', 'hard'])
        
        results = process_single_image(
            args.input, args.output, args.type, difficulty,
            platform=args.platform
        )
        for path, meta in results:
            print(f"  Created: {path} ({meta['forgery_type']}, {meta['difficulty']})")
    
    elif os.path.isdir(args.input):
        # Batch mode
        if args.difficulty:
            dist = {args.difficulty: 1.0}
        else:
            dist = {'easy': 0.3, 'medium': 0.4, 'hard': 0.3}
        
        batch_forge(
            args.input, args.output,
            forgery_type=args.type,
            difficulty_distribution=dist,
            platform=args.platform,
            seed=args.seed,
        )
    else:
        print(f"Error: '{args.input}' is not a valid file or directory")
        sys.exit(1)
