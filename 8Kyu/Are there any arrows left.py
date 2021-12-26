def any_arrows(arrows):
    if arrows == []: return False
    for i in arrows:
        if 'damaged' not in i.keys(): return True
        if i['damaged'] == False: return True
    return False