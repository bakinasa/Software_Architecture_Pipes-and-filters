import cv2
import numpy as np
from PIL import Image, ImageOps

# Filter for sepia application
def apply_sepia(frame):
    if not isinstance(frame, np.ndarray):
        raise ValueError("Input frame is not a valid NumPy array")
    
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepia_frame = cv2.transform(frame, sepia_filter)
    sepia_frame = np.clip(sepia_frame, 0, 255)
    return sepia_frame.astype(np.uint8)

# Filter for black and white image
def apply_grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Filter for specular reflection
def apply_mirror(frame):
    return cv2.flip(frame, 1)

# Filter for resizing
def apply_resize(frame, scale=0.75):
    height, width = frame.shape[:2]
    return cv2.resize(frame, (int(width * scale), int(height * scale)))

