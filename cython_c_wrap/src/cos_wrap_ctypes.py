""" Example of wrapping cos function from math.h using ctypes. 
Valentin Haenel, 2.8.3. Ctypes, Scipy Lectures, Oct 18 2016, [Online]
    Available: http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#id3
"""

import ctypes
import os

# find and load the library

if 'nt' == os.name:
    # Windows
    from ctypes import windll

    libm = windll.msvcrt
elif 'posix' == os.name:
    # OSX or linux
    from ctypes.util import find_library

    libm = ctypes.cdll.LoadLibrary(find_library('m'))
else:
    raise EnvironmentError('os.name = %s' % os.name)

# set the argument type
libm.cos.argtypes = [ctypes.c_double]
# set the return type
libm.cos.restype = ctypes.c_double


def cos_func(arg):
    ''' Wrapper for cos from math.h '''
    return libm.cos(arg)
