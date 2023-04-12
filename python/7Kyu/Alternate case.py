def alternate_case(s):
    temp = ''
    for i in s:
        if i.isupper() == True:
            temp += (i.lower())
        else:
            i.islower()
            temp += (i.upper())
    return temp