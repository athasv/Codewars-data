def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    return 0 if m < n else sum(range(n, m, n))
