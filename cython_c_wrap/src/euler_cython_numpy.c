#include    <assert.h>


double diff_eq(double xi){
    return -xi;
}


void euler_cython_c_function(double * result_t, double * result_x, const int size){
    // Simulation start and end time
    double ti = 0.0;
    double te = 10.0;

    double delta_t = 1e-3;

    // Initial state
    double x0 = 1.0;
    double dx_dt = 0.0;
    
    // Length of simulation
    const int n = (int) ((te - ti) / delta_t) + 1;

    // Check array size
    assert(size > n);

    // Set initial value    
    result_t[0] = ti;
    result_x[0] = x0;
    
    // Time step loop
    // Watch the last value of i here
    for (int i=0; (n-1)>i; ++i){
        // Calculate derivative
        dx_dt = diff_eq(result_x[i]);
        // Calculate state value of the next step
        result_x[i+1] = result_x[i] + dx_dt * delta_t;
        // Calculate time of next step
        result_t[i+1] = result_t[i] + delta_t;
    }

    return;
}
