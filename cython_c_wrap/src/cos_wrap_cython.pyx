""" Example of wrapping cos function from math.h using Cython. 
Valentin Haenel, 2.8.5. Cython, Scipy Lectures, Oct 18 2016, [Online]
    Available: http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#id3
"""

cdef extern from "math.h":
    double  cos(double arg)

def cos_func_cython(arg):
    return cos(arg)
