def remainder(a,b):
    min = a if a < b else b
    max = a if a > b else b
    return None if min == 0 else max - min*(max//min)