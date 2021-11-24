def digital_root(n):
    if n < 10:
         return n
    return digital_root(sum([int(c) for c in list(str(n))]))