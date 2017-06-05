/*
    2.8.4.1. Example, 2.8.4. SWIG, http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#id8
*/

#include <math.h>

double cos_func_swig(double arg){
    return cos(arg);
}
