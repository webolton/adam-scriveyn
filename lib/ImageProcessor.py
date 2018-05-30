# -*- coding: utf-8 -*-

''' Divide MS images into single pages; name images '''

import os
import imageio

def rename_images_in_directory(input_dir):
    # future params: input_dir, begin_index, begin_side, lacunae={}
    img_dir = directory = os.fsencode(input_dir)
    imgs = []
    for file in os.listdir(img_dir):
        filename = os.fsdecode(file)
        print(filename)

def split_and_rename_image(img_path, out_dir, ms_siglum, page_number=0):
    """
    Bisects, renames, and saves new images of MS pages

    Args:
        img_path (str): the directory and name of image.
        out_dir (str): the directory that the two new images will be stored in.
        ms_siglum (str): the abbreviated siglum of the MS, according to Görlach.
        page_number (int): the page number for the file name.
        lacunae (dic): a dictionary of the possible lacunae in the MS.
    """

    verso_no = 2
    recto_no = 3

    # Load the image
    img = imageio.imread(img_path)
    height, width, _ = img.shape

    # Cut the image in half
    width_cutoff = width // 2
    side1 = img[:, :width_cutoff, :]
    side2 = img[:, width_cutoff:, :]

    # Save the two halves
    imageio.imwrite(f"{out_dir}/{ms_siglum}_{verso_no}v.jpg", side1)
    imageio.imwrite(f"{out_dir}/{ms_siglum}_{recto_no}r.jpg", side2)

    return(height, width)

if __name__ == '__main__':
    main()
