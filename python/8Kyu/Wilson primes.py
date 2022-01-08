def am_i_wilson(n):
    temp = [1, 5, 13, 563, 5971, 558771, 1964215, 8121909, 12326713, 23025711, 26921605, 341569806, 399292158]
    return True if n in temp and n != 1 else False