import math
import unittest

import cos_cython_numpy
import numpy as np


class TestCosWrapBase(unittest.TestCase):
    def run_test_float(self, f):
        angle_deg_range = range(-360, 361)
        for angle_deg in angle_deg_range:
            angle_rad = math.radians(angle_deg)
            expected = math.cos(angle_rad)
            result = f(angle_rad)

            self.assertAlmostEqual(expected, result,
                                   msg='function = %r\nangle = %d (deg)' % (f, angle_deg))

    def run_test_float_wrong_arg(self, f, exception):
        with self.assertRaises(exception):
            f('foo')

    def run_test_numpy_cos(self, f):
        angle_deg_array = np.arange(-360, 361)
        angle_rad_array = np.deg2rad(angle_deg_array)
        result_array = np.empty_like(angle_rad_array)
        # a little different
        f(angle_rad_array, result_array)
        expected_array = np.cos(angle_rad_array)
        for angle_deg, result, expected in zip(angle_deg_array, result_array, expected_array):
            self.assertAlmostEqual(expected, result, msg='angle = %d (deg)' % angle_deg)

    def run_test_numpy_cos_wrong_argument(self, f, exception):
        with self.assertRaises(exception):
            f('foo', 'goo')


class TestCosWrapCython(TestCosWrapBase):
    def test_cos_cython_numpy(self):
        self.run_test_numpy_cos(cos_cython_numpy.cos_cython_numpy_py_func)

    def test_cos_cython_numpy_wrong_argument(self):
        self.run_test_numpy_cos_wrong_argument(cos_cython_numpy.cos_cython_numpy_py_func, TypeError)


class TestLsame(unittest.TestCase):
    def test_lsame(self):
        in_txt_0 = 'abc'
        in_txt_1 = 'abc'
        in_txt_2 = 'def'

        self.assertTrue(cos_cython_numpy.lsame_numpy_func(in_txt_0, in_txt_1))
        self.assertFalse(cos_cython_numpy.lsame_numpy_func(in_txt_0, in_txt_2))


if __name__ == '__main__':
    unittest.main()
