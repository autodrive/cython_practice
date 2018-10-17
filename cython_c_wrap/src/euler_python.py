def diff_eq_python(xi):

    # dx/dt + x = 0
    return -xi


def euler_python():

    # initial values
    ti = 0.0
    te = 10.0
    delta_t = 1e-3
    x0 = 1.0
    
    n = int((te - ti) / delta_t) + 1
    i = 0
    
    result_t = [0.0] * 10001
    result_x = [0.0] * 10001
    
    result_t[0] = ti
    result_x[0] = x0
    
    dx_dt = 0
    
    for i in range(1, n):
        dx_dt = diff_eq_python(result_x[i-1])
        result_x[i] = result_x[i-1] + dx_dt * delta_t
        result_t[i] = result_t[i-1] + delta_t

    return result_t, result_x
