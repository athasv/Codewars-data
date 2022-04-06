def remove(s):
    if not s.endswith('!'): return s
    for i,j in enumerate(s[::-1]):
        if j is not '!':
            return s[:-i]