def points(games):
    temp = []
    for i in games:
        i = i.split(":")
        temp.append(3) if int(i[0]) > int(i[1]) else (temp.append(1) if int(i[0]) == int(i[1]) else temp)
    return sum(temp)