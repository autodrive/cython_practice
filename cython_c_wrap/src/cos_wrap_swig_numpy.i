/*  Example of wrapping a C function that takes a C double array as input using
 *  numpy typemaps for SWIG.
 2.8.4.2. Numpy Support, 2.8.4. SWIG, http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#id9
*/

%module cos_wrap_swig_numpy
%{
    /* the resulting C file should be built as a python extension */
    #define SWIG_FILE_WITH_INIT
    /*  Includes the header in the wrapper code */
    #include "cos_wrap_swig_numpy.h"
%}

/*  include the numpy typemaps */
%include "numpy.i"
/*  need this for correct module initialization */
%init %{
    import_array();
%}

/*  typemaps for the two arrays, the second will be modified in-place */
%apply (double* IN_ARRAY1, int DIM1) {(double * in_array, int size_in)}
%apply (double* INPLACE_ARRAY1, int DIM1) {(double * out_array, int size_out)}

/*  Wrapper for cos_wrap_swig_numpy that massages the types */
%inline %{
    /*  takes as input two numpy arrays */
    void cos_func_swig_numpy(double * in_array, int size_in, double * out_array, int size_out) {
        /*  calls the original funcion, providing only the size of the first */
        cos_wrap_swig_numpy(in_array, out_array, size_in);
    }
%}
