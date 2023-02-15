def sum_array(arr):
    return sum(__import__("numpy").sort(arr)[1:-1]) if arr else 0