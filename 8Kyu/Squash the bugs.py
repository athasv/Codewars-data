def find_longest(string):
    spl = string.split(" ")
    temp = len(spl[0]) if spl else 0
    for word in spl[1:]:
        if temp < len(word):
            temp = len(word) 
    return temp