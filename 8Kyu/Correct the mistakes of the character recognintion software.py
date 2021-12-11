def correct(s):
    return s.translate(s.maketrans("015", "OIS"))