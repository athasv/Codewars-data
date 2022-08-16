def who_is_paying(name):
    temp = []
    temp.append(name)
    if (name==[]): return ['']
    if len(name) > 2: 
        temp.append(name[0]+name[1])
    return temp