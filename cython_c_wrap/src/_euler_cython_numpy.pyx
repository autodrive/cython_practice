""" Valentin Haenel, 2.8.5.2. Numpy Support, 2.8.5. Cython, Scipy Lectures, Oct 18 2016, [Online] 
        Available: http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#id13 
"""

# cimport the Cython declarations for numpy
cimport numpy as np

# if you want to use the Numpy-C-API from Cython
# (not strictly necessary for this example, but good practice)
np.import_array()

# cdefine the signature of our c function
cdef extern from "euler_cython_numpy.h":
    void euler_cython_c_function (double * result_t, double * result_x, int size)

# create the wrapper code, with numpy type annotations
def euler_cython_numpy_py_func(np.ndarray[double, ndim=1, mode="c"] in_array not None,
                     np.ndarray[double, ndim=1, mode="c"] out_array not None):
    euler_cython_c_function(<double*> np.PyArray_DATA(in_array),
                <double*> np.PyArray_DATA(out_array),
                in_array.shape[0])