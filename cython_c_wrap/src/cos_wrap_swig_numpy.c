/*
2.8.4.2. Numpy Support, 2.8.4. SWIG, http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#id9
*/

#include <math.h>

/*  Compute the cosine of each element in in_array, storing the result in
 *  out_array. */
void cos_func_swig_numpy(double * in_array, double * out_array, int size){
    int i;
    for(i=0;i<size;i++){
        out_array[i] = cos(in_array[i]);
    }
}
