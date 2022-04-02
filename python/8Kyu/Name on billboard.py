def billboard(name, price=30):
    return len(''.join( [name for i in range(price)] ) )