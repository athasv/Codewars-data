import numpy as np
def square_or_square_root(arr):
    test = []
    for i in arr:
        x = np.sqrt(i)
        if(x.is_integer()): 
            test.append(x)
        else: 
            test.append(np.power(i, 2))
    return test