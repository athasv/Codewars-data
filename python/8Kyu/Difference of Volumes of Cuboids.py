def find_difference(a, b):
    from functools import reduce
    return abs(reduce((lambda x, y: x * y), a) - reduce((lambda x, y: x * y), b))
