def textin(s):
    arr = ['two','Two','tWo','twO','TWo','tWO','TwO','TWO','TOO','too','toO','tOo','Too','ToO','TOo','tOO','to','To','tO','TO']
    for i in arr:
        s = s.replace(i,'2')
    return s
