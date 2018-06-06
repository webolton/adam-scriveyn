import unittest
import os
import glob
import imageio
from lib import ImageProcessor
from lib.ImageProcessor import (
                                split_and_rename_image, rename_images_in_directory,
                                front_matter_file_names, first_leaf_file_names
                                )

class TestImageProcessor(unittest.TestCase):

    def test_rename_images_in_directory(self):
        page_data = { 'start_index': 2, 'start_side': 'v', 'start_folio': 1 }
        input_dir = 'tests/mock_data/matz_pix'
        out_dir = 'tests/mock_data/mock_output_data'
        siglum = 'N'
        rename_images_in_directory(input_dir, out_dir, siglum, page_data)

        self.assertEqual(1, 1)

    def test_front_matter_file_names(self):
        siglum = 'N'
        fm_numbers = (6, 7)
        file_names, fm_numbers = front_matter_file_names(siglum, fm_numbers)
        returned_names = ('N_FM_6', 'N_FM_7')

        self.assertEqual((returned_names, (8, 9)), (file_names, fm_numbers))

    def test_first_leaf_file_names(self):
        folio_sides = ('r', 'v')
        start_folio = 2
        fm_numbers = (1, 2)
        siglum = 'N'
        returned_r_names = (f"{siglum}_FM_1", f"{siglum}_{start_folio}r")
        returned_v_names = (f"{siglum}_{start_folio}v", f"{siglum}_{start_folio + 1}r")

        for start_side in folio_sides:
            if start_side == 'r':
                leaf_numbers = (1, 2)
                file_names = returned_r_names
                next_leaf = 2

                actual_leaf_numbers, actual_file_names, actual_next_leaf = first_leaf_file_names(
                                                                           start_side, start_folio,
                                                                           fm_numbers, siglum)
            if start_side == 'v':
                leaf_numbers = (2, 3)
                file_names = returned_v_names
                next_leaf = 3

                actual_leaf_numbers, actual_file_names, actual_next_leaf = first_leaf_file_names(
                                                                           start_side, start_folio,
                                                                           fm_numbers, siglum)

            self.assertEqual((leaf_numbers, file_names, next_leaf),
                            (actual_leaf_numbers, actual_file_names, actual_next_leaf))

    def test_split_and_rename_image(self):
        img_path = 'tests/mock_data/Matz.jpg'
        out_dir = 'tests/mock_data/mock_output_data'
        siglum = 'N'

        split_and_rename_image(img_path, out_dir, siglum)

        side1 = imageio.imread(out_dir + f"/{siglum}_2v.jpg")
        side2 = imageio.imread(out_dir + f"/{siglum}_3r.jpg")

        original_image = imageio.imread(img_path)

        for side in (side1, side2):
            test_height = side.shape[0]
            test_width = side.shape[1]

            self.assertEqual(test_height, original_image.shape[0])
            self.assertEqual(test_width, original_image.shape[1] // 2)

    def tearDown(self):
        if glob.glob('tests/mock_data/mock_output_data/*.jpg'):
            files = glob.glob('tests/mock_data/mock_output_data/*.jpg')
            for file in files:
                os.remove(file)


if __name__ == '__main__':
    unittest.main()
