def next_id(arr):
    c = 0
    for i in sorted(set(arr)):
        if i != c:
            return c
        c += 1
    return c
