/*  Example of wrapping cos function from math.h with the Python-C-API.
Valentin Haenel, 2.8.2. Python-C-Api, Scipy Lectures, Oct 18 2016, [Online]
    Available: http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#example*/

#include <Python.h>
#include <math.h>

/*  wrapped cosine function */
static PyObject* cos_func(PyObject* self, PyObject* args)
{
    double value;
    double answer;

    /*  parse the input, from python float to c double */
    if (!PyArg_ParseTuple(args, "d", &value))
        return NULL;
    /* if the above function returns -1, an appropriate Python exception will
     * have been set, and the function simply returns NULL
     */

    /* call cos from libm */
    answer = cos(value);

    /*  construct the output from cos, from c double to python float */
    return Py_BuildValue("f", answer);
}

/*  define functions in module */
static PyMethodDef CosMethods[] =
{
     {"cos_func", cos_func, METH_VARARGS, "evaluate the cosine"},
     {NULL, NULL, 0, NULL}
};
/*
Extending Embedded Python
https://docs.python.org/3/extending/embedding.html?highlight=pymethoddef#extending-embedded-python

iCodez, Compiler can't find Py_InitModule() .. is it deprecated and if so what should I use?, stackoverflow.com, Feb 3 2015, [Online] Available: https://stackoverflow.com/questions/28305731/compiler-cant-find-py-initmodule-is-it-deprecated-and-if-so-what-should-i
*/
static struct PyModuleDef cos_wrap =
{
    PyModuleDef_HEAD_INIT,
    "cos_wrap", /* name of module */
    "",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    CosMethods
};


/* module initialization */
PyMODINIT_FUNC

PyInit_cos_wrap(void)
{
     (void) PyModule_Create(&cos_wrap);
}
