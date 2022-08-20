def char_freq(message):
    temp = {}
    for i in sorted(message):
        temp[i] = message.count(i)
    return temp