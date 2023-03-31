import math

def isMultiple(a, b, n):
    dec, _ = math.modf(a / b)
    dec = math.floor(10 * dec + 0.5)
    return False if not dec or dec >= 10 else dec % n == 0