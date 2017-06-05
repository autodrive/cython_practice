import ctypes
import math
import unittest

import cos_wrap  # Python-C-API
import cos_wrap_ctypes  # ctypes
import cos_wrap_ctypes_numpy  # ctypes NumPy support
import cos_wrap_swig  # SWIG
import cos_wrap_swig_numpy  # SWIG NumPy support
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

    def run_test_numpy(self, f):
        angle_deg_array = np.arange(-360, 361)
        angle_rad_array = np.deg2rad(angle_deg_array)
        result_array = np.empty_like(angle_rad_array)

        # a little different
        f(angle_rad_array, result_array)
        expected_array = np.cos(angle_rad_array)

        for angle_deg, result, expected in zip(angle_deg_array, result_array, expected_array):
            self.assertAlmostEqual(expected, result, msg='function = %r\nangle = %d (deg)' % (f, angle_deg))


class TestCosWrap(TestCosWrapBase):
    def test_cos(self):
        self.run_test_float(cos_wrap.cos_func)

    def test_cos_wrong_argument(self):
        self.run_test_float_wrong_arg(cos_wrap.cos_func, TypeError)


class TestCosWrapCtype(TestCosWrapBase):
    def test_ctypes_cos(self):
        self.run_test_float(cos_wrap_ctypes.cos_func)

    def test_ctypes_cos_wrong_argument(self):
        self.run_test_float_wrong_arg(cos_wrap_ctypes.cos_func, ctypes.ArgumentError)

    def test_ctypes_numpy_cos(self):
        self.run_test_numpy(cos_wrap_swig_numpy.cos_func_swig_numpy)

    def test_ctypes_numpy_cos_wrong_argument(self):
        with self.assertRaises(ctypes.ArgumentError):
            cos_wrap_ctypes_numpy.cos_doubles_ctypes('foo', 'goo')


class TestCosWrapSwig(TestCosWrapBase):
    def test_cos(self):
        self.run_test_float(cos_wrap_swig.cos_func_swig)

    def test_cos_wrong_argument(self):
        self.run_test_float_wrong_arg(cos_wrap_swig.cos_func_swig, TypeError)

    def test_swig_numpy_cos(self):
        self.run_test_numpy(cos_wrap_swig_numpy.cos_func_swig_numpy)


if __name__ == '__main__':
    unittest.main()
