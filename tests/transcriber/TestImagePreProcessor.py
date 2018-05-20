import unittest
from transcriber import ImagePreProcessor
from transcriber.ImagePreProcessor import load_image

class TestImagePreProcessor(unittest.TestCase):

    def test_load_image(self):
        data_list = ('JPEG', (3520, 3136), 'RGB')
        res = load_image()
        self.assertEqual(res, data_list)

if __name__ == '__main__':
    unittest.main()
