def two_sort(array):
    array.sort()
    temp = array[0]
    result = ""
    for i in temp:
        result += i + "***"
    result = result[0:-3]
    return result
        
        