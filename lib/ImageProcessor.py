# Resize manuscript images
import os, sys
from PIL import Image

def load_image():
    """
    First step in making this program
    """
    img = Image.open('images/N_73v_74r.JPG')
    image_info = (img.format, img.size, img.mode)
    print(image_info)
    return image_info

def main():
    load_image()

if __name__ == '__main__':
    main()
