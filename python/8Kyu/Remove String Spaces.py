def no_space(x):
    return x.translate(str.maketrans('', '', ' \n\t\r'))