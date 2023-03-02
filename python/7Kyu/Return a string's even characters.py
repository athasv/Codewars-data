def even_chars(st): 
    if len(st) >= 2 and len(st) <= 100:
        return [x for x in st[1::2]]
    return "invalid string"
        