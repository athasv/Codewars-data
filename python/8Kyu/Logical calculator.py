def logical_calc(array, op):
    if op == "AND":
        return all(array)
    if op == "OR":
        return any(array)
    return __import__("functools").reduce(lambda x, y: x ^ y, array)