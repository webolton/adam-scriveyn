# Resize manuscript images
import os, sys
from PIL import Image

def load_image():
    img = Image.open('images/N_73v_74r.JPG')
    print(img.format, img.size, img.mode)
