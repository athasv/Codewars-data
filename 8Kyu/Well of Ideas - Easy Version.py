def well(x):
    if x.count('good') > 2: return 'I smell a series!'
    if x.count('good') in range(1,3): return 'Publish!'
    if x.count('bad') >=1: return 'Fail!'