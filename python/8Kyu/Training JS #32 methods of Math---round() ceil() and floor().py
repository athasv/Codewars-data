def round_it(n):
    val = str(n)
    dec_pos = val.find('.')
    dec_val = val[(dec_pos+1):]
    if(len(dec_val) >  len(val[0:dec_pos])): return __import__("math").ceil(n)
    if(len(dec_val) <  len(val[0:dec_pos])): return __import__("math").floor(n)
    if(len(dec_val) == len(val[0:dec_pos])): return __import__("numpy").round(n,0)
    