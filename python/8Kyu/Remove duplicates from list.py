def distinct(seq):
    temp = [ii for n,ii in enumerate(seq) if ii not in seq[:n]]
    return temp