/*  Example of wrapping cos function from math.h using SWIG.
    2.8.4.1. Example, 2.8.4. SWIG, http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#id8
*/

%module cos_wrap_swig
%{
    /* the resulting C file should be built as a python extension */
    #define SWIG_FILE_WITH_INIT
    /*  Includes the header in the wrapper code */
    #include "cos_wrap_swig.h"
%}

/*  Parse the header file to generate wrappers */
%include "cos_wrap_swig.h"
