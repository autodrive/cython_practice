# Valentin Haenel, 2.8.2.1. Example, 2.8.2. Python-C-Api, Scipy Lectures, Oct 18 2016, [Online]
#   Available: http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#example
# Valentin Haenel, 2.8.4.1. Example, 2.8.4. SWIG, Scipy Lectures, Oct 18 2016, [Online]
#   Available: , http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#id8

from distutils.core import setup, Extension

# define the extension module for Python-C-API
cos_wrap = Extension('cos_wrap', sources=['cos_wrap.c'])

# for SWIG
cos_wrap_swig = Extension("_cos_wrap_swig", sources=["cos_wrap_swig.c", "cos_wrap_swig.i"])

# for SWIG NumPy Support
cos_wrap_swig_numpy = Extension("_cos_wrap_swig_numpy", sources=["cos_wrap_swi_numpyg.c", "cos_wrap_swig_numpy.i"])

# run the setup
setup(ext_modules=[cos_wrap, cos_wrap_swig, cos_wrap_swig_numpy])
