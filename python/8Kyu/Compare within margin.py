def close_compare(a, b, margin=0):
    if __import__("numpy").abs(a - b) <= margin: return 0
    if a > b: return 1
    if a < b: return -1