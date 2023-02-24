def is_square(n):    
    return __import__("math").sqrt(n).is_integer() if n >= 0 else False