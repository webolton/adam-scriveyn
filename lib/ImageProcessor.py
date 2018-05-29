# Divide MS images into single pages; name images
import os, sys
from PIL import Image

def split_and_rename_images(img_path):
    """
    Split and rename images
    """

    img = Image.open(img_path)
    image_info = (img.format, img.size, img.mode)
    print(image_info)
    return image_info

if __name__ == '__main__':
    main()
