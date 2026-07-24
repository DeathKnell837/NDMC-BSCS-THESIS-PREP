"""
Error Level Analysis (ELA) Module — ForgeGuard Thesis System
============================================================
Performs Error Level Analysis on receipt images to highlight JPEG compression
discontinuities caused by image editing / digital forgery.

Algorithm:
1. Re-save the original image as a JPEG at a specific quality (default: 90/95).
2. Compute pixel-wise absolute difference between original and re-saved image.
3. Scale the difference for visual enhancement (default scale factor: 15-20x).
4. Return enhanced ELA image (as PIL Image or NumPy array).
"""

import io
import numpy as np
from PIL import Image, ImageChops, ImageEnhance

def compute_ela(image: Image.Image, quality: int = 90, scale: float = 15.0) -> Image.Image:
    """
    Computes Error Level Analysis (ELA) for a PIL Image.
    
    Args:
        image: PIL Image object (RGB mode).
        quality: JPEG compression quality for re-saving (1-100, default 90).
        scale: Multiplier factor to amplify error differences (default 15.0).
        
    Returns:
        PIL Image: ELA visual representation.
    """
    # Ensure RGB mode
    if image.mode != 'RGB':
        image = image.convert('RGB')
        
    # Re-save image in memory as JPEG at target quality
    buffer = io.BytesIO()
    image.save(buffer, format='JPEG', quality=quality)
    buffer.seek(0)
    
    # Load re-compressed image
    resaved_image = Image.open(buffer).convert('RGB')
    
    # Calculate pixel-wise absolute difference
    ela_diff = ImageChops.difference(image, resaved_image)
    
    # Find max brightness to scale appropriately, or use fixed scale
    extrema = ela_diff.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    
    if max_diff == 0:
        max_diff = 1
        
    # Enhance difference brightness for visual contrast
    enhancer = ImageEnhance.Brightness(ela_diff)
    ela_image = enhancer.enhance(scale)
    
    return ela_image

def generate_ela_image(image: Image.Image, quality: int = 90, scale: float = 15.0) -> Image.Image:
    """Alias for compute_ela."""
    return compute_ela(image, quality=quality, scale=scale)


def evaluate_ela_forgery_risk(ela_image: Image.Image) -> dict:
    """
    Evaluates pixel variance and error level distribution to estimate forgery risk.
    
    Returns:
        dict: {'mean': float, 'variance': float, 'max': float, 'is_suspicious': bool}
    """
    arr = np.array(ela_image, dtype=np.float32)
    mean_val = float(np.mean(arr))
    var_val = float(np.var(arr))
    max_val = float(np.max(arr))
    
    # Suspicious threshold: high variance in re-compression error
    is_suspicious = var_val > 185.0 or max_val > 210.0
    
    return {
        'mean': mean_val,
        'variance': var_val,
        'max': max_val,
        'is_suspicious': is_suspicious
    }
