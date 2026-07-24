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

def mask_name_gcash(full_name):
    """
    Format name in GCash Express Send style: GW••••••N D.
    """
    parts = full_name.split()
    if len(parts) >= 2:
        first = parts[0]
        last = parts[-1]
        if len(first) >= 2:
            masked_first = first[:2] + "••••••" + first[-1]
        else:
            masked_first = first + "••••••"
        return f"{masked_first.upper()} {last[0].upper()}."
    return f"{full_name[:2].upper()}••••••{full_name[-1].upper()}"


def draw_express_send_receipt(receipt_data, add_artifacts=False, artifact_type=None):
    """
    Draw authentic GCash 'Express Send' receipt image (Modern 2024-2026 Layout).
    Matches official GCash mobile receipt format 1:1.
    """
    img = Image.new('RGB', (RECEIPT_WIDTH, RECEIPT_HEIGHT), GCASH_BLUE)
    draw = ImageDraw.Draw(img)
    
    # Fonts
    font_header_title = get_font('bold', 46)
    font_name_large = get_font('segoe_bold', 52)
    font_phone = get_font('segoe_bold', 38)
    font_sub = get_font('regular', 32)
    font_label = get_font('segoe_bold', 38)
    font_val = get_font('segoe_bold', 40)
    font_total_label = get_font('segoe_bold', 40)
    font_total_val = get_font('segoe_bold', 56)
    font_ref = get_font('segoe_bold', 36)
    font_date = get_font('regular', 32)
    font_eco_bold = get_font('segoe_bold', 36)
    font_eco_text = get_font('regular', 28)
    font_download = get_font('segoe_bold', 40)
    
    y = 0
    
    # --- STATUS BAR ---
    draw.rectangle([0, 0, RECEIPT_WIDTH, 80], fill=GCASH_BLUE)
    status_time = receipt_data['datetime'].strftime("%I:%M").lstrip('0')
    draw.text((50, 20), status_time, fill=GCASH_WHITE, font=get_font('segoe_bold', 32))
    draw.text((RECEIPT_WIDTH - 240, 20), "86.5 KB/s 📶 4G  66%", fill=GCASH_WHITE, font=get_font('regular', 26))
    
    y = 80
    
    # --- HEADER BAR ---
    header_h = 130
    # Close icon X on left
    draw.text((60, y + 25), "✕", fill=GCASH_WHITE, font=get_font('bold', 48))
    # Title centered
    title = "Express Send"
    bbox = draw.textbbox((0, 0), title, font=font_header_title)
    tw = bbox[2] - bbox[0]
    draw.text(((RECEIPT_WIDTH - tw) // 2, y + 25), title, fill=GCASH_WHITE, font=font_header_title)
    
    y += header_h
    
    # --- WHITE RECEIPT CARD ---
    card_x1 = 50
    card_x2 = RECEIPT_WIDTH - 50
    card_w = card_x2 - card_x1
    card_top = y
    card_bottom = card_top + 1420
    
    # Rounded top card
    draw.rounded_rectangle([card_x1, card_top, card_x2, card_bottom], radius=40, fill=GCASH_WHITE)
    
    # --- CHECKMARK CIRCLE ---
    cx = RECEIPT_WIDTH // 2
    circle_y = card_top + 30
    circle_r = 65
    # Outer blue circle
    draw.ellipse([cx - circle_r, circle_y, cx + circle_r, circle_y + circle_r * 2], fill=(0, 105, 230))
    # White check mark
    draw.text((cx - 24, circle_y + 22), "✓", fill=GCASH_WHITE, font=get_font('bold', 70))
    
    y = circle_y + circle_r * 2 + 50
    
    # --- RECIPIENT MASKED NAME ---
    raw_name = receipt_data['recipient_name']
    masked_name_str = mask_name_gcash(raw_name)
    
    if add_artifacts and artifact_type == 'name_modification':
        # Forgery: altered recipient name
        masked_name_str = mask_name_gcash("Daniela S. Ungab")
    
    bbox = draw.textbbox((0, 0), masked_name_str, font=font_name_large)
    tw = bbox[2] - bbox[0]
    draw.text(((RECEIPT_WIDTH - tw) // 2, y), masked_name_str, fill=(0, 75, 185), font=font_name_large)
    
    y += 80
    
    # --- PHONE NUMBER PILL ---
    phone_raw = receipt_data.get('recipient_phone', '+63 975 343 9451')
    if not phone_raw.startswith('+63'):
        phone_clean = phone_raw.replace(' ', '')
        if phone_clean.startswith('0'):
            phone_raw = f"+63 {phone_clean[1:4]} {phone_clean[4:7]} {phone_clean[7:]}"
        else:
            phone_raw = f"+63 {phone_raw}"
            
    phone_str = phone_raw
    bbox = draw.textbbox((0, 0), phone_str, font=font_phone)
    tw = bbox[2] - bbox[0]
    pill_w = tw + 80
    pill_h = 70
    pill_x1 = (RECEIPT_WIDTH - pill_w) // 2
    pill_y1 = y
    draw.rounded_rectangle([pill_x1, pill_y1, pill_x1 + pill_w, pill_y1 + pill_h], radius=35, fill=(238, 244, 255))
    draw.text(((RECEIPT_WIDTH - tw) // 2, pill_y1 + 12), phone_str, fill=(0, 70, 170), font=font_phone)
    
    y += pill_h + 20
    
    # --- SUBTITLE ---
    sub_str = "Sent via GCash"
    bbox = draw.textbbox((0, 0), sub_str, font=font_sub)
    tw = bbox[2] - bbox[0]
    draw.text(((RECEIPT_WIDTH - tw) // 2, y), sub_str, fill=(160, 165, 175), font=font_sub)
    
    y += 65
    
    # DIVIDER 1
    draw.line([card_x1 + 60, y, card_x2 - 60, y], fill=(225, 230, 238), width=2)
    y += 45
    
    # --- AMOUNT ROW ---
    left_m = card_x1 + 60
    right_m = card_x2 - 60
    
    draw.text((left_m, y), "Amount", fill=(20, 30, 55), font=font_label)
    
    amt_val = receipt_data['amount']
    amt_str = f"{amt_val:,.2f}" if isinstance(amt_val, (int, float)) else str(amt_val)
    
    if add_artifacts and artifact_type == 'amount_alteration':
        amt_str = "5,000.00"
        
    bbox = draw.textbbox((0, 0), amt_str, font=font_val)
    tw = bbox[2] - bbox[0]
    draw.text((right_m - tw, y), amt_str, fill=(20, 30, 55), font=font_val)
    
    y += 85
    
    # DIVIDER 2
    draw.line([card_x1 + 60, y, card_x2 - 60, y], fill=(225, 230, 238), width=2)
    y += 45
    
    # --- TOTAL AMOUNT SENT ROW ---
    draw.text((left_m, y + 8), "Total Amount Sent", fill=(20, 30, 55), font=font_total_label)
    
    # Format amount with 'P' prefix safely to avoid missing glyph box [?] on Linux
    total_str = f"P{amt_str}"
    bbox = draw.textbbox((0, 0), total_str, font=font_total_val)
    tw = bbox[2] - bbox[0]
    draw.text((right_m - tw, y), total_str, fill=(0, 75, 185), font=font_total_val)
    
    y += 120
    
    # --- REF NO & TIMESTAMP SECTION ---
    ref_num = receipt_data.get('ref_number', '2043 210 185624')
    if add_artifacts and artifact_type == 'ref_fabrication':
        ref_num = '9948 102 773819'
    elif len(ref_num.replace(' ', '')) == 13:
        clean_ref = ref_num.replace(' ', '')
        ref_num = f"{clean_ref[:4]} {clean_ref[4:7]} {clean_ref[7:]}"
        
    ref_str = f"Ref No. {ref_num}"
    bbox = draw.textbbox((0, 0), ref_str, font=font_ref)
    tw = bbox[2] - bbox[0]
    draw.text(((RECEIPT_WIDTH - tw) // 2, y), ref_str, fill=(90, 105, 130), font=font_ref)
    
    y += 55
    
    dt_obj = receipt_data.get('datetime', datetime.now())
    date_str = dt_obj.strftime("%b %d, %Y %I:%M %p").replace(" 0", " ")
    bbox = draw.textbbox((0, 0), date_str, font=font_date)
    tw = bbox[2] - bbox[0]
    draw.text(((RECEIPT_WIDTH - tw) // 2, y), date_str, fill=(120, 130, 150), font=font_date)
    
    y += 95
    
    # --- GREEN CARBON FOOTPRINT CARD (gCO2e) ---
    eco_x1 = card_x1 + 50
    eco_x2 = card_x2 - 50
    eco_y1 = y
    eco_h = 220
    draw.rounded_rectangle([eco_x1, eco_y1, eco_x2, eco_y1 + eco_h], radius=24, fill=(162, 232, 206))
    
    # Eco text content
    draw.text((eco_x1 + 40, eco_y1 + 30), "🍃 279g (gCO2e)", fill=(10, 80, 50), font=font_eco_bold)
    
    eco_caption1 = "By going digital, you reduce your carbon footprint"
    eco_caption2 = "from transportation, paper, and plastic."
    draw.text((eco_x1 + 40, eco_y1 + 95), eco_caption1, fill=(15, 95, 60), font=font_eco_text)
    draw.text((eco_x1 + 40, eco_y1 + 140), eco_caption2, fill=(15, 95, 60), font=font_eco_text)
    
    # --- RECEIPT SAWTOOTH TEAR LINE (BOTTOM EDGE OF WHITE CARD) ---
    tear_y = card_bottom
    saw_w = 30
    saw_h = 25
    for x_pos in range(card_x1, card_x2, saw_w):
        poly = [
            (x_pos, tear_y),
            (x_pos + saw_w // 2, tear_y + saw_h),
            (x_pos + saw_w, tear_y)
        ]
        draw.polygon(poly, fill=GCASH_BLUE)
        
    # --- DOWNLOAD BUTTON AT BOTTOM ---
    btn_y = card_bottom + 100
    down_str = "⤓  Download"
    bbox = draw.textbbox((0, 0), down_str, font=font_download)
    tw = bbox[2] - bbox[0]
    draw.text(((RECEIPT_WIDTH - tw) // 2, btn_y), down_str, fill=GCASH_WHITE, font=font_download)
    
    return img


def draw_gcash_receipt(receipt_data, add_artifacts=False, artifact_type=None, style='express_send'):
    """
    Unified GCash receipt renderer supporting modern Express Send and Classic layouts.
    """
    if style == 'express_send' or True:
        return draw_express_send_receipt(receipt_data, add_artifacts=add_artifacts, artifact_type=artifact_type)


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
