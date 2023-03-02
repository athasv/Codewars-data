def unique(integers):
    pass
    temp = []
    for i in integers:
        if i not in temp:
            temp.append(i)
    return temp