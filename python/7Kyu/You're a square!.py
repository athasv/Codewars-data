def is_square(n): 
    if n>0  or n == 0:
        if int(n ** 0.5 + 0.5) ** 2 == n:
            return True
        return False
    if n < 0:
        return False