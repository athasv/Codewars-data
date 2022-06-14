def stairs_in_20(stairs):
    oneYear = 0
    if stairs is not None:
        for i in stairs:
            for j in i:
                oneYear += j
        return oneYear * 20
    else:
        return "Error"