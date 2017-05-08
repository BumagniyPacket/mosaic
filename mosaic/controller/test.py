import unittest

from PIL import Image

from mosaic.controller.Image2Mosaic import (normalize_image,
                                            MINIMAL_SHAPE)


class TestMosaic(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_normalize_image_function(self):
        normal_image = Image.new('L', [450, 450])
        small_image = Image.new('L', [20, 20])

        test_image = normalize_image(normal_image)
        self.assertTrue(min(test_image.size) > MINIMAL_SHAPE)
        self.assertEqual(normal_image.size, test_image.size)

        test_image = normalize_image(small_image)
        self.assertEqual(min(test_image.size), MINIMAL_SHAPE)
        self.assertNotEqual(small_image.size, test_image.size)


if __name__ == '__main__':
    unittest.main()
