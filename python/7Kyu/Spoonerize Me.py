def spoonerize(words):
    temp = words.split(" ")
    w1, w2 = temp[0], temp[1]
    wl1 = [char for char in w1] + [" "]
    wl2 = [char for char in w2]
    wl1[0], wl2[0] = wl2[0], wl1[0]
    return "".join(wl1) + "".join(wl2)