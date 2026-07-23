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

def convert_ela_to_array(ela_image: Image.Image, target_size: tuple = (224, 224)) -> np.ndarray:
    """
    Resizes and normalizes ELA image for CNN model input.
    
    Args:
        ela_image: PIL Image returned by compute_ela.
        target_size: Target tuple (height, width), default (224, 224).
        
    Returns:
        np.ndarray: Normalized array of shape (target_size[0], target_size[1], 3) in range [0, 1].
    """
    resized = ela_image.resize(target_size, Image.Resampling.BILINEAR)
    arr = np.array(resized, dtype=np.float32) / 255.0
    return arr
