# Valentin Haenel, 2.8.2.1. Example, 2.8.2. Python-C-Api, Scipy Lectures, Oct 18 2016, [Online]
#   Available: http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#example
# Valentin Haenel, 2.8.4.1. Example, 2.8.4. SWIG, Scipy Lectures, Oct 18 2016, [Online]
#   Available: , http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#id8

import re
import urllib.request as requests
from distutils.core import setup, Extension

import numpy

cos_wrap = Extension('cos_wrap', sources=['cos_wrap.c'])

# for SWIG
cos_wrap_swig = Extension("_cos_wrap_swig", sources=["cos_wrap_swig.c", "cos_wrap_swig.i"])

# https://stackoverflow.com/questions/21855775/numpy-i-is-missing-what-is-the-recommended-way-to-install-it
np_version = re.compile(r'(?P<MAJOR>[0-9]+)\.'
                        '(?P<MINOR>[0-9]+)') \
    .search(numpy.__version__)
np_version_string = np_version.group()
np_version_info = {key: int(value)
                   for key, value in list(np_version.groupdict().items())}

np_file_name = 'numpy.i'
np_file_url = 'https://raw.githubusercontent.com/numpy/numpy/maintenance/' + \
              np_version_string + '.x/tools/swig/' + np_file_name
if (np_version_info['MAJOR'] == 1 and np_version_info['MINOR'] < 9):
    np_file_url = np_file_url.replace('tools', 'doc')

chunk_size = 8196
with open(np_file_name, 'wb') as file:
    with requests.urlopen(np_file_url) as remote:
        file.write(remote.read())

# for SWIG NumPy Support
# https://github.com/hmmlearn/hmmlearn/issues/43#issuecomment-138609372
print("numpy.get_include() = %r" % numpy.get_include())
cos_wrap_swig_numpy = Extension("_cos_wrap_swig_numpy",
                                sources=["cos_wrap_swig_numpy.c", "cos_wrap_swig_numpy.i"],
                                include_dir=[numpy.get_include()])

# run the setup
setup(ext_modules=[cos_wrap, cos_wrap_swig, cos_wrap_swig_numpy], include_dir=[numpy.get_include()])
