def in_array(array1, array2):
    temp = []
    for i in array1:
        for j in array2:
            if i in j and i not in temp:
                temp.append(i)
    return sorted(set(temp))