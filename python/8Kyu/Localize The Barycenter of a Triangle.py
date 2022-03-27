def bar_triang(x, y, z):
    temp = (x,y,z)
    store = [round((temp[0][0] + temp[1][0] + temp[2][0]) / 3, 4),round((temp[0][1] + temp[1][1] + temp[2][1]) / 3, 4)]
    return store