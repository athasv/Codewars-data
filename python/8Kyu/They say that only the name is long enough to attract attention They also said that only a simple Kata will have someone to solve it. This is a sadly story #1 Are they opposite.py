def is_opposite(s1,s2):
    if not s1 or s1.lower() != s2.lower(): return False
    for i, v in enumerate(s1):
        if v == s2[i]: return False
    return True