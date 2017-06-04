# Valentin Haenel, 2.8.2. Python-C-Api, Scipy Lectures, Oct 18 2016, [Online]
#   Available: http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#example

from distutils.core import setup, Extension

# define the extension module
cos_wrap = Extension('cos_wrap', sources=['cos_wrap.c'])

# run the setup
setup(ext_modules=[cos_wrap])
