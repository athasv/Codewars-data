def pythagorean_triple(integers):
    integers.sort()
    return True if integers[0]**2 + integers[1]**2 == integers[2]**2 else False