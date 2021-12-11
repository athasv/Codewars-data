def getVolumeOfCubiod(length, width, height):
    temp = length * width * height
    return temp if isinstance(temp, int) else float("{:.2f}".format(temp))