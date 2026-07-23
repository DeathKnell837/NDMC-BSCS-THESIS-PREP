"""
GCash Receipt Generator — Thesis Dataset Tool
===============================================
Generates authentic-looking and forged GCash "Send Money" receipt images
for training CNN models (Basic CNN, ResNet50, MobileNetV2).

Forgery Types:
  1. Amount alteration (modified transaction value)
  2. Reference number fabrication (fake transaction IDs)
  3. Recipient/sender name modification
  4. Full template-based fabrication (entirely fake receipts)

Usage:
  python gcash_receipt_generator.py --output ./dataset --authentic 500 --forged 500
"""

import os
import sys
import random
import string
import argparse
import json
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont

# ============================================================
# CONFIGURATION
# ============================================================

# GCash brand colors
GCASH_BLUE = (0, 100, 210)         # Primary blue
GCASH_DARK_BLUE = (0, 70, 160)     # Header/top bar
GCASH_LIGHT_BG = (245, 247, 250)   # Light gray background
GCASH_WHITE = (255, 255, 255)
GCASH_GREEN = (0, 180, 80)         # Success checkmark
GCASH_TEXT_DARK = (30, 30, 30)     # Primary text
GCASH_TEXT_GRAY = (130, 130, 130)  # Secondary text
GCASH_TEXT_LIGHT = (180, 180, 180) # Tertiary text
GCASH_DIVIDER = (220, 220, 225)    # Divider lines

# Receipt dimensions (mobile screenshot proportions)
RECEIPT_WIDTH = 1080
RECEIPT_HEIGHT = 1920

# Font paths (Windows)
FONTS_DIR = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')

def get_font(name, size):
    """Load a font cross-platform (Windows/Linux), falling back to sized default."""
    font_map = {
        'bold': 'arialbd.ttf',
        'regular': 'arial.ttf',
        'italic': 'ariali.ttf',
        'light': 'segoeuil.ttf',
        'segoe': 'segoeui.ttf',
        'segoe_bold': 'segoeuib.ttf',
    }
    
    font_filename = font_map.get(name, 'arial.ttf')
    is_bold = 'bold' in name
    
    # Common Linux font search paths
    search_paths = [
        FONTS_DIR,
        '/usr/share/fonts/truetype/dejavu',
        '/usr/share/fonts/truetype/liberation',
        '/usr/share/fonts/truetype/freefont',
        '/usr/share/fonts/TTF',
        '/usr/share/fonts'
    ]
    
    # 1. Try exact font filename across search paths
    for s_dir in search_paths:
        if not s_dir or not os.path.exists(s_dir):
            continue
        p = os.path.join(s_dir, font_filename)
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
                
    # 2. Try Linux DejaVu or Liberation fallback
    fallback_fonts = ['DejaVuSans-Bold.ttf' if is_bold else 'DejaVuSans.ttf',
                      'LiberationSans-Bold.ttf' if is_bold else 'LiberationSans-Regular.ttf']
    for s_dir in search_paths:
        if not s_dir or not os.path.exists(s_dir):
            continue
        for ff in fallback_fonts:
            p = os.path.join(s_dir, ff)
            if os.path.exists(p):
                try:
                    return ImageFont.truetype(p, size)
                except Exception:
                    pass

    # 3. Modern Pillow load_default(size=size)
    try:
        return ImageFont.load_default(size=size)
    except Exception:
        return ImageFont.load_default()

# ============================================================
# DATA POOLS
# ============================================================

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
    "Bacanto", "Ungab", "Mariano", "Tenebroso", "Hontiveros",
    "Manalo", "Pascual", "Salazar", "Aguilar", "Mercado", "Bondad",
]

COMMON_AMOUNTS = [
    50, 100, 150, 200, 250, 300, 350, 400, 450, 500,
    600, 700, 750, 800, 900, 1000, 1200, 1500, 1800,
    2000, 2500, 3000, 3500, 4000, 4500, 5000,
    6000, 7000, 7500, 8000, 9000, 10000,
]

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def random_name():
    """Generate a random Filipino full name."""
    first = random.choice(FILIPINO_FIRST_NAMES)
    last = random.choice(FILIPINO_LAST_NAMES)
    # Sometimes include middle initial
    if random.random() > 0.5:
        middle = random.choice(string.ascii_uppercase)
        return f"{first} {middle}. {last}"
    return f"{first} {last}"

def random_phone():
    """Generate a random Philippine mobile number."""
    prefix = random.choice(["0917", "0918", "0919", "0920", "0921",
                           "0927", "0928", "0929", "0930", "0935",
                           "0936", "0937", "0938", "0939", "0940",
                           "0941", "0942", "0943", "0945", "0946",
                           "0947", "0948", "0949", "0950", "0951",
                           "0953", "0954", "0955", "0956", "0961",
                           "0963", "0965", "0966", "0967", "0975",
                           "0976", "0977", "0978", "0979", "0991",
                           "0992", "0993", "0994", "0995", "0996",
                           "0997", "0998", "0999"])
    remaining = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    return f"{prefix} {remaining[:3]} {remaining[3:]}"

def masked_phone(phone):
    """Mask middle digits of phone number: 0917 ***  4321."""
    parts = phone.split()
    if len(parts) == 3:
        return f"{parts[0]} *** {parts[2]}"
    return phone

def random_ref_number():
    """Generate a GCash-style reference number (13 digits)."""
    return ''.join([str(random.randint(0, 9)) for _ in range(13)])

def random_amount():
    """Generate a realistic transaction amount."""
    if random.random() > 0.3:
        return random.choice(COMMON_AMOUNTS)
    else:
        return round(random.uniform(20, 15000), 2)

def random_datetime():
    """Generate a random datetime within the last 90 days."""
    now = datetime.now()
    days_ago = random.randint(0, 90)
    hours = random.randint(6, 23)
    minutes = random.randint(0, 59)
    dt = now - timedelta(days=days_ago)
    dt = dt.replace(hour=hours, minute=minutes, second=random.randint(0, 59))
    return dt

def format_amount(amount):
    """Format amount with peso sign and commas: ₱1,500.00"""
    if amount == int(amount):
        return f"₱{int(amount):,}.00"
    return f"₱{amount:,.2f}"

def format_date(dt):
    """Format date: Jul 22, 2026"""
    return dt.strftime("%b %d, %Y")

def format_time(dt):
    """Format time: 08:45 PM"""
    return dt.strftime("%I:%M %p")

# ============================================================
# RECEIPT DRAWING ENGINE
# ============================================================

def draw_gcash_receipt(receipt_data, add_artifacts=False, artifact_type=None):
    """
    Draw a complete GCash 'Send Money' receipt image.
    
    Args:
        receipt_data: dict with transaction details
        add_artifacts: bool — if True, introduce forgery artifacts
        artifact_type: str — type of forgery artifact to add
    
    Returns:
        PIL.Image object
    """
    img = Image.new('RGB', (RECEIPT_WIDTH, RECEIPT_HEIGHT), GCASH_LIGHT_BG)
    draw = ImageDraw.Draw(img)
    
    # Fonts
    font_title = get_font('bold', 52)
    font_amount_large = get_font('bold', 80)
    font_label = get_font('regular', 36)
    font_value = get_font('segoe', 38)
    font_value_bold = get_font('segoe_bold', 38)
    font_small = get_font('regular', 30)
    font_tiny = get_font('light', 26)
    font_header = get_font('segoe_bold', 40)
    
    y = 0
    
    # --- STATUS BAR (top) ---
    draw.rectangle([0, 0, RECEIPT_WIDTH, 80], fill=(0, 0, 0))
    # Time on status bar
    status_time = receipt_data['datetime'].strftime("%I:%M")
    draw.text((40, 20), status_time, fill=GCASH_WHITE, font=get_font('segoe_bold', 32))
    # Battery/signal icons (simplified)
    draw.text((RECEIPT_WIDTH - 200, 20), "4G  🔋", fill=GCASH_WHITE, font=get_font('regular', 30))
    
    y = 80
    
    # --- GCASH BLUE HEADER ---
    header_height = 180
    draw.rectangle([0, y, RECEIPT_WIDTH, y + header_height], fill=GCASH_BLUE)
    
    # Back arrow
    draw.text((30, y + 20), "←", fill=GCASH_WHITE, font=get_font('bold', 50))
    
    # "GCash" centered in header
    gcash_text = "GCash"
    bbox = draw.textbbox((0, 0), gcash_text, font=get_font('segoe_bold', 48))
    text_w = bbox[2] - bbox[0]
    draw.text(((RECEIPT_WIDTH - text_w) // 2, y + 20), gcash_text,
              fill=GCASH_WHITE, font=get_font('segoe_bold', 48))
    
    # "Send Money" subtitle
    subtitle = "Send Money"
    bbox = draw.textbbox((0, 0), subtitle, font=get_font('regular', 36))
    text_w = bbox[2] - bbox[0]
    draw.text(((RECEIPT_WIDTH - text_w) // 2, y + 80), subtitle,
              fill=(200, 220, 255), font=get_font('regular', 36))
    
    y += header_height + 30
    
    # --- WHITE CARD (main receipt body) ---
    card_x = 40
    card_w = RECEIPT_WIDTH - 80
    card_top = y
    card_height = 1350
    
    # Draw rounded-corner card (simplified with rectangle)
    draw.rounded_rectangle([card_x, card_top, card_x + card_w, card_top + card_height],
                          radius=30, fill=GCASH_WHITE)
    
    y = card_top + 50
    cx = RECEIPT_WIDTH // 2  # center x
    
    # --- SUCCESS CHECKMARK ---
    circle_r = 55
    draw.ellipse([cx - circle_r, y - 5, cx + circle_r, y + circle_r * 2 - 5],
                fill=GCASH_GREEN)
    # Checkmark
    draw.text((cx - 25, y + 5), "✓", fill=GCASH_WHITE, font=get_font('bold', 65))
    
    y += circle_r * 2 + 25
    
    # --- "Sent Successfully" ---
    sent_text = "Sent Successfully!"
    bbox = draw.textbbox((0, 0), sent_text, font=font_title)
    text_w = bbox[2] - bbox[0]
    draw.text(((RECEIPT_WIDTH - text_w) // 2, y), sent_text,
              fill=GCASH_TEXT_DARK, font=font_title)
    
    y += 80
    
    # --- AMOUNT ---
    amount_str = format_amount(receipt_data['amount'])
    bbox = draw.textbbox((0, 0), amount_str, font=font_amount_large)
    text_w = bbox[2] - bbox[0]
    
    if add_artifacts and artifact_type == 'amount_alteration':
        # Forgery: slightly different font size or color mismatch
        forged_font = get_font('bold', random.choice([76, 78, 82, 84]))
        draw.text(((RECEIPT_WIDTH - text_w) // 2, y), amount_str,
                  fill=GCASH_TEXT_DARK, font=forged_font)
    else:
        draw.text(((RECEIPT_WIDTH - text_w) // 2, y), amount_str,
                  fill=GCASH_BLUE, font=font_amount_large)
    
    y += 110
    
    # --- DIVIDER ---
    draw.line([card_x + 60, y, card_x + card_w - 60, y], fill=GCASH_DIVIDER, width=2)
    y += 30
    
    # --- TRANSACTION DETAILS ---
    left_margin = card_x + 70
    right_margin = card_x + card_w - 70
    line_height = 85
    
    details = [
        ("Sent to", receipt_data['recipient_name']),
        ("Mobile Number", receipt_data['recipient_phone_masked']),
        ("Ref. No.", receipt_data['ref_number']),
        ("Date", format_date(receipt_data['datetime'])),
        ("Time", format_time(receipt_data['datetime'])),
    ]
    
    for label, value in details:
        # Label (left, gray)
        draw.text((left_margin, y), label, fill=GCASH_TEXT_GRAY, font=font_label)
        
        # Value (right-aligned, dark)
        bbox = draw.textbbox((0, 0), str(value), font=font_value_bold)
        text_w = bbox[2] - bbox[0]
        
        if add_artifacts and artifact_type == 'ref_fabrication' and label == "Ref. No.":
            # Forgery: slightly misaligned or different font
            draw.text((right_margin - text_w + random.randint(-3, 3),
                      y + random.randint(-2, 2)),
                     str(value), fill=GCASH_TEXT_DARK,
                     font=get_font('regular', random.choice([36, 37, 39, 40])))
        elif add_artifacts and artifact_type == 'name_modification' and label == "Sent to":
            # Forgery: name with subtle font inconsistency
            draw.text((right_margin - text_w, y), str(value),
                     fill=(25, 25, 25),  # Slightly different shade
                     font=get_font('bold', 38))
        else:
            draw.text((right_margin - text_w, y), str(value),
                     fill=GCASH_TEXT_DARK, font=font_value_bold)
        
        y += line_height
        
        # Light divider between rows
        if label != "Time":
            draw.line([left_margin, y - 20, right_margin, y - 20],
                     fill=(240, 240, 242), width=1)
    
    y += 30
    
    # --- SERVICE FEE ---
    draw.line([card_x + 60, y, card_x + card_w - 60, y], fill=GCASH_DIVIDER, width=2)
    y += 25
    
    draw.text((left_margin, y), "Service Fee", fill=GCASH_TEXT_GRAY, font=font_label)
    fee_text = "FREE"
    bbox = draw.textbbox((0, 0), fee_text, font=font_value_bold)
    text_w = bbox[2] - bbox[0]
    draw.text((right_margin - text_w, y), fee_text,
             fill=GCASH_GREEN, font=font_value_bold)
    
    y += line_height
    
    # --- TOTAL AMOUNT ---
    draw.text((left_margin, y), "Total", fill=GCASH_TEXT_DARK, font=font_header)
    total_str = format_amount(receipt_data['amount'])
    bbox = draw.textbbox((0, 0), total_str, font=font_header)
    text_w = bbox[2] - bbox[0]
    draw.text((right_margin - text_w, y), total_str,
             fill=GCASH_TEXT_DARK, font=font_header)
    
    y += line_height + 20
    
    # --- REMAINING BALANCE ---
    balance_text = f"Remaining Balance: {format_amount(receipt_data['balance'])}"
    bbox = draw.textbbox((0, 0), balance_text, font=font_small)
    text_w = bbox[2] - bbox[0]
    draw.text(((RECEIPT_WIDTH - text_w) // 2, y), balance_text,
             fill=GCASH_TEXT_GRAY, font=font_small)
    
    y += 70
    
    # --- ACTION BUTTONS ---
    btn_y = card_top + card_height + 40
    btn_w = 460
    btn_h = 80
    
    # "Send Again" button
    btn1_x = (RECEIPT_WIDTH // 2) - btn_w - 20
    draw.rounded_rectangle([btn1_x, btn_y, btn1_x + btn_w, btn_y + btn_h],
                          radius=40, outline=GCASH_BLUE, width=3)
    sa_text = "Send Again"
    bbox = draw.textbbox((0, 0), sa_text, font=font_value_bold)
    tw = bbox[2] - bbox[0]
    draw.text((btn1_x + (btn_w - tw) // 2, btn_y + 18), sa_text,
             fill=GCASH_BLUE, font=font_value_bold)
    
    # "Done" button
    btn2_x = (RECEIPT_WIDTH // 2) + 20
    draw.rounded_rectangle([btn2_x, btn_y, btn2_x + btn_w, btn_y + btn_h],
                          radius=40, fill=GCASH_BLUE)
    done_text = "Done"
    bbox = draw.textbbox((0, 0), done_text, font=font_value_bold)
    tw = bbox[2] - bbox[0]
    draw.text((btn2_x + (btn_w - tw) // 2, btn_y + 18), done_text,
             fill=GCASH_WHITE, font=font_value_bold)
    
    # --- BOTTOM NAV BAR ---
    nav_y = RECEIPT_HEIGHT - 140
    draw.rectangle([0, nav_y, RECEIPT_WIDTH, RECEIPT_HEIGHT], fill=GCASH_WHITE)
    draw.line([0, nav_y, RECEIPT_WIDTH, nav_y], fill=GCASH_DIVIDER, width=2)
    
    nav_items = ["Home", "Promos", "Scan QR", "Inbox", "Profile"]
    nav_spacing = RECEIPT_WIDTH // len(nav_items)
    for i, item in enumerate(nav_items):
        bbox = draw.textbbox((0, 0), item, font=font_tiny)
        tw = bbox[2] - bbox[0]
        x = i * nav_spacing + (nav_spacing - tw) // 2
        color = GCASH_BLUE if item == "Home" else GCASH_TEXT_GRAY
        draw.text((x, nav_y + 60), item, fill=color, font=font_tiny)
        # Simple icon placeholder (dot)
        draw.ellipse([x + tw // 2 - 8, nav_y + 20, x + tw // 2 + 8, nav_y + 50],
                    fill=color)
    
    # --- FORGERY: Full template artifacts ---
    if add_artifacts and artifact_type == 'full_template':
        # Add subtle compression-like noise
        import numpy as np
        arr = np.array(img)
        noise = np.random.normal(0, random.uniform(2, 5), arr.shape).astype(np.int16)
        arr = np.clip(arr.astype(np.int16) + noise, 0, 255).astype(np.uint8)
        img = Image.fromarray(arr)
    
    return img


def generate_receipt_data():
    """Generate a random but realistic set of receipt data."""
    amount = random_amount()
    phone = random_phone()
    balance = round(random.uniform(50, 50000), 2)
    
    return {
        'amount': amount,
        'recipient_name': random_name(),
        'recipient_phone': phone,
        'recipient_phone_masked': masked_phone(phone),
        'ref_number': random_ref_number(),
        'datetime': random_datetime(),
        'balance': balance,
        'service_fee': 0.0,
    }


def generate_forged_receipt_data(authentic_data, forgery_type):
    """
    Create a forged version of authentic receipt data.
    
    Args:
        authentic_data: dict of original receipt data
        forgery_type: str — 'amount', 'ref_number', 'name', 'full_template'
    
    Returns:
        Modified receipt data dict
    """
    forged = authentic_data.copy()
    
    if forgery_type == 'amount':
        # Change amount to a different value
        original_amount = forged['amount']
        while True:
            new_amount = random_amount()
            if new_amount != original_amount:
                break
        forged['amount'] = new_amount
    
    elif forgery_type == 'ref_number':
        # Generate a completely fake reference number
        forged['ref_number'] = random_ref_number()
    
    elif forgery_type == 'name':
        # Change recipient name
        original_name = forged['recipient_name']
        while True:
            new_name = random_name()
            if new_name != original_name:
                break
        forged['recipient_name'] = new_name
    
    elif forgery_type == 'full_template':
        # Completely new fake receipt
        forged = generate_receipt_data()
    
    return forged


# ============================================================
# DATASET GENERATION
# ============================================================

def generate_dataset(output_dir, num_authentic=500, num_forged=500, 
                     include_compressed=True, seed=42):
    """
    Generate a complete dataset of authentic and forged receipts.
    
    Directory structure:
        output_dir/
        ├── authentic/
        │   ├── highres/
        │   └── compressed/
        ├── forged/
        │   ├── highres/
        │   │   ├── amount_alteration/
        │   │   ├── ref_fabrication/
        │   │   ├── name_modification/
        │   │   └── full_template/
        │   └── compressed/
        │       ├── amount_alteration/
        │       ├── ref_fabrication/
        │       ├── name_modification/
        │       └── full_template/
        └── metadata.json
    """
    random.seed(seed)
    
    forgery_types = ['amount', 'ref_number', 'name', 'full_template']
    artifact_map = {
        'amount': 'amount_alteration',
        'ref_number': 'ref_fabrication',
        'name': 'name_modification',
        'full_template': 'full_template',
    }
    
    # Create directory structure
    dirs = [
        os.path.join(output_dir, 'authentic', 'highres'),
        os.path.join(output_dir, 'authentic', 'compressed'),
    ]
    for ft in artifact_map.values():
        dirs.append(os.path.join(output_dir, 'forged', 'highres', ft))
        dirs.append(os.path.join(output_dir, 'forged', 'compressed', ft))
    
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    
    metadata = {
        'total_authentic': num_authentic,
        'total_forged': num_forged,
        'forgery_types': list(artifact_map.values()),
        'includes_compressed': include_compressed,
        'seed': seed,
        'generated_at': datetime.now().isoformat(),
        'images': []
    }
    
    print(f"Generating {num_authentic} authentic receipts...")
    for i in range(num_authentic):
        data = generate_receipt_data()
        img = draw_gcash_receipt(data, add_artifacts=False)
        
        # Save high-res
        fname = f"authentic_{i+1:04d}.png"
        img.save(os.path.join(output_dir, 'authentic', 'highres', fname), 'PNG')
        
        # Save compressed version
        if include_compressed:
            comp_fname = f"authentic_{i+1:04d}.jpg"
            quality = random.randint(25, 45)  # Simulate messaging app compression
            img.save(os.path.join(output_dir, 'authentic', 'compressed', comp_fname),
                    'JPEG', quality=quality)
        
        metadata['images'].append({
            'filename': fname,
            'class': 'authentic',
            'amount': data['amount'],
            'ref_number': data['ref_number'],
            'recipient': data['recipient_name'],
        })
        
        if (i + 1) % 50 == 0:
            print(f"  ✓ {i+1}/{num_authentic} authentic receipts generated")
    
    print(f"\nGenerating {num_forged} forged receipts...")
    forged_per_type = num_forged // len(forgery_types)
    remainder = num_forged % len(forgery_types)
    
    forged_count = 0
    for ft_idx, ft in enumerate(forgery_types):
        count = forged_per_type + (1 if ft_idx < remainder else 0)
        artifact_name = artifact_map[ft]
        artifact_type_map = {
            'amount': 'amount_alteration',
            'ref_number': 'ref_fabrication',
            'name': 'name_modification',
            'full_template': 'full_template',
        }
        
        for j in range(count):
            forged_count += 1
            authentic_data = generate_receipt_data()
            forged_data = generate_forged_receipt_data(authentic_data, ft)
            img = draw_gcash_receipt(forged_data, add_artifacts=True,
                                     artifact_type=artifact_type_map[ft])
            
            # Save high-res
            fname = f"forged_{artifact_name}_{j+1:04d}.png"
            img.save(os.path.join(output_dir, 'forged', 'highres', artifact_name, fname), 'PNG')
            
            # Save compressed version
            if include_compressed:
                comp_fname = f"forged_{artifact_name}_{j+1:04d}.jpg"
                quality = random.randint(25, 45)
                img.save(os.path.join(output_dir, 'forged', 'compressed', artifact_name, comp_fname),
                        'JPEG', quality=quality)
            
            metadata['images'].append({
                'filename': fname,
                'class': 'forged',
                'forgery_type': artifact_name,
                'amount': forged_data['amount'],
                'ref_number': forged_data['ref_number'],
                'recipient': forged_data['recipient_name'],
            })
        
        print(f"  ✓ {count} {artifact_name} forgeries generated")
    
    # Save metadata
    meta_path = os.path.join(output_dir, 'metadata.json')
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False, default=str)
    
    print(f"\n{'='*50}")
    print(f"Dataset generation complete!")
    print(f"  Authentic: {num_authentic} images")
    print(f"  Forged:    {num_forged} images ({forged_per_type} per type × {len(forgery_types)} types)")
    print(f"  Total:     {num_authentic + num_forged} images")
    if include_compressed:
        print(f"  + Compressed versions: {num_authentic + num_forged} additional images")
    print(f"  Metadata:  {meta_path}")
    print(f"{'='*50}")


# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate GCash receipt dataset for CNN forgery detection training'
    )
    parser.add_argument('--output', type=str, default='./dataset',
                       help='Output directory for generated images (default: ./dataset)')
    parser.add_argument('--authentic', type=int, default=500,
                       help='Number of authentic receipts to generate (default: 500)')
    parser.add_argument('--forged', type=int, default=500,
                       help='Number of forged receipts to generate (default: 500)')
    parser.add_argument('--no-compressed', action='store_true',
                       help='Skip generating compressed versions')
    parser.add_argument('--seed', type=int, default=42,
                       help='Random seed for reproducibility (default: 42)')
    parser.add_argument('--preview', action='store_true',
                       help='Generate just 1 authentic + 1 forged receipt for preview')
    
    args = parser.parse_args()
    
    if args.preview:
        print("Generating preview receipts...")
        os.makedirs(args.output, exist_ok=True)
        
        # Authentic
        data = generate_receipt_data()
        img = draw_gcash_receipt(data)
        preview_path = os.path.join(args.output, 'preview_authentic.png')
        img.save(preview_path, 'PNG')
        print(f"  ✓ Authentic: {preview_path}")
        
        # Forged (amount alteration)
        forged_data = generate_forged_receipt_data(data, 'amount')
        img_forged = draw_gcash_receipt(forged_data, add_artifacts=True,
                                        artifact_type='amount_alteration')
        preview_path2 = os.path.join(args.output, 'preview_forged_amount.png')
        img_forged.save(preview_path2, 'PNG')
        print(f"  ✓ Forged (amount): {preview_path2}")
        
        # Forged (full template)
        try:
            import numpy as np
            full_data = generate_receipt_data()
            img_full = draw_gcash_receipt(full_data, add_artifacts=True,
                                          artifact_type='full_template')
            preview_path3 = os.path.join(args.output, 'preview_forged_full.png')
            img_full.save(preview_path3, 'PNG')
            print(f"  ✓ Forged (full template): {preview_path3}")
        except ImportError:
            print("  ⚠ NumPy not installed, skipping full_template preview")
        
        print("\nDone! Check the preview images.")
    else:
        generate_dataset(
            output_dir=args.output,
            num_authentic=args.authentic,
            num_forged=args.forged,
            include_compressed=not args.no_compressed,
            seed=args.seed,
        )
