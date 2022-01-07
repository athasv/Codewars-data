def between(a,b):
    x = [*range(a, b + 1 , 1)]
    return [i for i in x if a <= i <= b]