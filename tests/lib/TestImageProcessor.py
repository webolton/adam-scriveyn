import unittest
from lib import ImageProcessor
from lib.ImageProcessor import split_and_rename_images

class TestImageProcessor(unittest.TestCase):

    def test_split_and_rename_images(self):
        img_path = 'tests/mock_data/Matz.jpg'
        data_list = ('JPEG', (320, 410), 'RGB')
        res = split_and_rename_images(img_path)
        self.assertEqual(res, data_list)

if __name__ == '__main__':
    unittest.main()
