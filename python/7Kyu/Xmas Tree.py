def xmastree(n):
    temp = []
    trunk = '_' * (n - 1) + '#' + '_' * (n - 1)
    for i in range(1, n + 1):
        _ = ''
        _ += '_' * (n - i) + '#' * (i * 2 - 1) + '_' * (n - i)
        temp.append(_)
    temp.extend([trunk, trunk])
    return temp