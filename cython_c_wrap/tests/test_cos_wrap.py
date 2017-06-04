import unittest
import cos_wrap
import math

import numpy as np


class TestCosWrap(unittest.TestCase):
    def test_cos(self):
        angle_deg_range = range(-360, 361)
        for angle_deg in angle_deg_range:
            angle_rad = math.radians(angle_deg)
            expected = math.cos(angle_rad)
            result = cos_wrap.cos_func(angle_rad)

            self.assertAlmostEqual(expected, result,
                                   msg='angle = %d (deg)' % angle_deg)

    def test_cos_wrong_argument(self):
        with self.assertRaises(TypeError):
            cos_wrap.cos_func('foo')

    def test_cos_np(self):
        angle_deg_array = np.arange(-360, 361)
        angle_rad_array = np.deg2rad(angle_deg_array)
        result_array = cos_wrap.cos_func_np(angle_rad_array)
        expected_array = np.cos(angle_rad_array)

        for angle_deg, expected, result in zip(angle_deg_array, result_array, expected_array):
            self.assertAlmostEqual(expected, result,
                               msg='angle = %d (deg)' % angle_deg)

    def test_cos_np_wrong_argument(self):
        with self.assertRaises(TypeError):
            cos_wrap.cos_func_np('foo')


if __name__ == '__main__':
    unittest.main()
