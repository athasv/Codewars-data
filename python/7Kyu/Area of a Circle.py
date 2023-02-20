def circle_area(r):
    return False if not isinstance(r, int) or r < 0 else round(__import__("numpy").pi*(r**2), 2)