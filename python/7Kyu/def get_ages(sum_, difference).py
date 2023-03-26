def get_ages(sum_, difference):
    a, b  = (sum_+difference)/2, (sum_-difference)/2
    return None if sum_<0 or difference<0 or a<0 or b<0 else(a,b)
