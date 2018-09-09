# -*- coding: utf-8 -*-

''' Divide MS images into single leaves; rename images. '''

import os
import imageio
import cv2

def crop_dp_spread(file, top, bottom, left, right):
    '''
    Returns a cropped image.

    Args:
        file (str): the path to the file to be cropped
        top (int): the amount to be cropped off the top margin
        bottom (int): the amount to be cropped off the bottom margin
        left (int): the amount to be cropped of the left margin
        right (int): the amount to be cropped of the right margin
    '''

    img = cv2.imread(file)
    height, width, _ = img.shape
    crop_img = img[top:height-bottom, left:width-right]
    return crop_img

def rename_images_in_directory(input_dir, out_dir, siglum, page_data, fm_numbers=(1, 2)):
    '''
    Loads a directory of MS images; iterates through the directory calling `split_and_rename_image`,
    the function that splits and renames them.

    Args:
        input_dir (str): the directory where original the images are.
        out_dir (str): the directory where the split and renamed images will be saved.
        siglum (str): the abbreviated siglum of the MS, according to Görlach.
        page_data (dic): a dictionary of metadata about the starting page / leaf. Should look like:
            { 'start_index': 9, 'start_side': 'r', 'start_folio': 1 }
        fm_numbers (tup): the beginning front matter pagination. Default args: (1, 2)
        TODO:
        lacunae (dic): metadata about missing leaves.
    '''

    start_index = page_data['start_index']
    start_side = page_data['start_side']
    start_folio = page_data['start_folio']

    img_dir = os.fsencode(input_dir)
    sorted_dir = sorted(os.listdir(img_dir))

    for index, file in enumerate(sorted_dir):

        img_path = f"{input_dir}/{os.fsdecode(file)}"

        # Get names for front matter and call split_and_rename_image
        if index < start_index:
            fm_numbers, file_names = front_matter_file_names(siglum, fm_numbers)
            split_and_rename_image(img_path, out_dir, file_names)

        # Get file names for the first paginated leaf call split_and_rename_image
        if index == start_index:
            leaf_numbers, file_names, next_leaf = first_leaf_file_names(start_side, start_folio,
                                                                        fm_numbers, siglum)
            split_and_rename_image(img_path, out_dir, file_names)

        # Get file names for the paginated leaves and call split_and_rename_image
        if index > start_index:
            leaf_numbers, file_names, next_leaf = paginated_leaves_file_names(next_leaf, siglum,
                                                                              leaf_numbers)
            split_and_rename_image(img_path, out_dir, file_names)

def front_matter_file_names(siglum, fm_numbers):
    '''
    Returns file names for front matter. Currently hard coded as FM plus a page no (not folio no).
    Args:
        siglum (str): the siglum for the MS.
        fm_numbers (tup): the front matter page numbers to be used in the file name.
    Returns:
        tuple:
            file_names (tup): file names for front matter pages in image.
            fm_numbers (tup): incremented front matter page references.
    '''

    file_names = (f"{siglum}_FM_{fm_numbers[0]}", f"{siglum}_FM_{fm_numbers[1]}")
    fm_numbers = (fm_numbers[0] + 2, fm_numbers[1] + 2)

    return(fm_numbers, file_names)

def first_leaf_file_names(start_side, start_folio, fm_numbers, siglum):
    '''
    Returns file names for first image containing first folio. When first folio starts on recto,
    front matter page is hard coded to FM.
    Args:
        start_side (str): the starting side of the folio. Can only be 'r' or 'v'.
        TODO: Assign recto and verso to constants.
        start_folio (int): the number of the first folio.
        fm_numbers (tup): the last fm_return for calculating a folio starting with 'r'
        siglum (str): the siglum for the MS.
    Returns:
        tuple:
            leaf_numbers (tup): assigns tuple of leaf numbers (int) for subsequent folios.
            file_names (tup): file names for first folio images.
            next_leaf (int): last leaf number to use as iterator.
    '''
    if start_side == 'r':
        leaf_numbers = (fm_numbers[0], start_folio)
        file_names = (f"{siglum}_FM_{leaf_numbers[0]}", f"{siglum}_{leaf_numbers[1]}r")
        next_leaf = leaf_numbers[1]

        return(leaf_numbers, file_names, next_leaf)

    if start_side == 'v':
        leaf_numbers = (start_folio, start_folio + 1)
        file_names = (f"{siglum}_{leaf_numbers[0]}v", f"{siglum}_{leaf_numbers[1]}r")
        next_leaf = leaf_numbers[1]

        return(leaf_numbers, file_names, next_leaf)

def paginated_leaves_file_names(next_leaf, siglum, leaf_numbers):
    '''
    Returns file names for folios following first.
    Args:
        next_leaf (int): starting number for foliation.
        siglum (str): the siglum for the MS.
        leaf_numbers (tup): assigns tuple of leaf numbers (int) for subsequent folios.
    Returns:
        leaf_numbers (tup): assigns tuple of leaf numbers (int) for subsequent folios.
        file_names (tup): file names for the folio images.
        next_leaf (int): iterator for continuing foliation.
    '''
    leaf_numbers = (next_leaf, next_leaf + 1)
    file_names = (f"{siglum}_{leaf_numbers[0]}v", f"{siglum}_{leaf_numbers[1]}r")
    next_leaf = leaf_numbers[1]

    return(leaf_numbers, file_names, next_leaf)

def split_and_rename_image(img_path, out_dir, file_names):
    """
    Bisects, renames, and saves new images of MS pages

    Args:
        img_path (str): the directory and name of image.
        out_dir (str): the directory that the two new images will be stored in.
        file_names (tup): the names for the two images.
    TODO:
        It might be worth while to detect the middle of the page, if simply cutting the image in
        half is not effective enough.
    """

    # Load the image
    img = imageio.imread(img_path)
    height, width, _ = img.shape

    # Cut the image in half
    width_cutoff = width // 2
    side1 = img[:, :width_cutoff, :]
    side2 = img[:, width_cutoff:, :]

    # Save the two halves
    cv2.imwrite(f"{out_dir}/{file_names[0]}.jpg", side1)
    cv2.imwrite(f"{out_dir}/{file_names[1]}.jpg", side2)

if __name__ == '__main__':
    main()
