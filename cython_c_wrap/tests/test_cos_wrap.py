import unittest
import cos_wrap
import math


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


if __name__ == '__main__':
    unittest.main()
