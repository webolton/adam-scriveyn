# -*- coding: utf-8 -*-

''' Divide MS images into single leaves; name images. '''

import os
import imageio

def rename_images_in_directory(input_dir, out_dir, siglum, page_data, fm_numbers=(1, 2)):
    '''
    Loads a directory of MS images; iterates through the directory calling `split_and_rename_image`,
    the function that splits and renames them.

    Args:
        input_dir (str): the directory where original the images are.
        out_dir (str): the directory where the split and renamed images will be saved.
        siglum (str): the siglum for the MS.
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
            file_names, fm_numbers = front_matter_file_names(siglum, fm_numbers)

        # Get file names for the first paginaged leaf call split_and_rename_image
        if index == start_index:
            leaf_numbers, file_names, next_leaf = first_leaf_file_names(start_side, start_folio,
                                                                        fm_numbers, siglum)

        # Get file names for the paginated leaves and call split_and_rename_image
        if index > start_index:
            leaf_numbers, file_names, next_leaf = paginated_leaves_file_names(next_leaf, siglum,
                                                                              leaf_numbers)

def front_matter_file_names(siglum, fm_numbers):
    '''
    Returns file names for front matter. Currently hard coded as FM plus a page no (not folio no)
    '''
    file_names = (f"{siglum}_FM_{fm_numbers[0]}", f"{siglum}_FM_{fm_numbers[1]}")
    fm_numbers = (fm_numbers[0] + 2, fm_numbers[1] + 2)

    return(file_names, fm_numbers)

def first_leaf_file_names(start_side, start_folio, fm_numbers, siglum):
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
    leaf_numbers = (next_leaf, next_leaf + 1)
    file_names = (f"{siglum}_{leaf_numbers[0]}v", f"{siglum}_{leaf_numbers[1]}r")
    next_leaf = leaf_numbers[1]

    return(leaf_numbers, file_names, next_leaf)

def split_and_rename_image(img_path, out_dir, siglum, page_number=0):
    """
    Bisects, renames, and saves new images of MS pages

    Args:
        img_path (str): the directory and name of image.
        out_dir (str): the directory that the two new images will be stored in.
        siglum (str): the abbreviated siglum of the MS, according to Görlach.
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
    imageio.imwrite(f"{out_dir}/{siglum}_{verso_no}v.jpg", side1)
    imageio.imwrite(f"{out_dir}/{siglum}_{recto_no}r.jpg", side2)

    return(height, width)

if __name__ == '__main__':
    main()
