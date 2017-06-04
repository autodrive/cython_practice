import ctypes
import math
import unittest

import cos_wrap
import cos_wrap_ctypes
import cos_wrap_ctypes_numpy  # ctypes NumPy support
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

    def test_ctypes_cos(self):
        angle_deg_range = range(-360, 361)
        for angle_deg in angle_deg_range:
            angle_rad = math.radians(angle_deg)
            expected = math.cos(angle_rad)
            result = cos_wrap_ctypes.cos_func(angle_rad)

            self.assertAlmostEqual(expected, result,
                                   msg='angle = %d (deg)' % angle_deg)

    def test_ctypes_cos_wrong_argument(self):
        with self.assertRaises(ctypes.ArgumentError):
            cos_wrap_ctypes.cos_func('foo')

    def test_ctypes_numpy_cos(self):
        angle_deg_array = np.arange(-360, 361)
        angle_rad_array = np.deg2rad(angle_deg_array)
        result_array = np.empty_like(angle_rad_array)

        # a little different
        cos_wrap_ctypes_numpy.cos_doubles_ctypes(angle_rad_array, result_array)
        expected_array = np.cos(angle_rad_array)

        for angle_deg, result, expected in zip(angle_deg_array, result_array, expected_array):
            self.assertAlmostEqual(expected, result, msg='angle = %d (deg)' % angle_deg)

    def test_ctypes_numpy_cos_wrong_argument(self):
        with self.assertRaises(ctypes.ArgumentError):
            cos_wrap_ctypes_numpy.cos_doubles_ctypes('foo', 'goo')


if __name__ == '__main__':
    unittest.main()
