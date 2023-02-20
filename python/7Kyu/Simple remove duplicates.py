def solve(arr): 
    cache = set()
    out = []
    for item in arr[::-1]:
        if item in cache:
            continue
        cache.add(item)
        out.append(item)
    return out[::-1]