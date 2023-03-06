def is_triangle(a, b, c):
    if a >0 and b> 0 and c> 0:
        return a + b > c and b + c > a and a + c > b
    return False
        
