def _all(seq, fun): 
    return sum(fun(x) for x in seq) == len(seq)