def is_divide_by(number, a, b):
    import numpy as np
    return True if np.abs(number) % np.abs(a) == 0 and np.abs(number) % np.abs(b) == 0 else False 