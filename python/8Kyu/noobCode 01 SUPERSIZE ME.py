def super_size(n):
    temp =[x for x in str(n)]
    return int("".join(sorted(temp, reverse=True)))