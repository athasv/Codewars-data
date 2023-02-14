def position(alphabet):
    pass
    temp = (__import__("string").ascii_lowercase).find( alphabet.lower() )
    return "Position of alphabet: {}".format( temp + 1 )