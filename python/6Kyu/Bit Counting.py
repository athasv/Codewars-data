def count_bits(n):
    bits = 0
    for one in '{0:b}'.format(n):
        if one is '1':
            bits += 1
    return bits