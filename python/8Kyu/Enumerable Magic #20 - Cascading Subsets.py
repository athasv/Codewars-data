def each_cons(lst, n):
    temp = []
    for i in range(0, len(lst)-n+1):
        temp.append(lst[i:i+n])
    return temp