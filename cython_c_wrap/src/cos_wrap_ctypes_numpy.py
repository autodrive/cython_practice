""" Example of wrapping a C library function that accepts a C double array as
    input using the numpy.ctypeslib. 
    2.8.3.2. Numpy Support, 2.8.3. Ctypes, http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#id6
"""

import os
from ctypes import c_int

import numpy as np
import numpy.ctypeslib as npct

# input type for the cos_doubles_ctypes function
# must be a double array, with single dimension that is contiguous
array_1d_double = npct.ndpointer(dtype=np.double, ndim=1, flags='CONTIGUOUS')

# https://stackoverflow.com/questions/7162366/get-location-of-the-py-source-file
library_path = os.path.dirname(os.path.abspath(__file__))
library_name = "libcos_doubles_ctypes"

try:
    # load the library, using numpy mechanisms
    libcd = npct.load_library(library_name, library_path)
except OSError as e:
    print('os.listdir(library_path):')
    print(os.listdir(library_path))
    raise e

# setup the return types and argument types
libcd.cos_doubles_ctypes.restype = None
libcd.cos_doubles_ctypes.argtypes = [array_1d_double, array_1d_double, c_int]


def cos_doubles_ctypes(in_array, out_array):
    return libcd.cos_doubles_ctypes(in_array, out_array, len(in_array))
