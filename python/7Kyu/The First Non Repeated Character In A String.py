def first_non_repeated(s):
    for _ in s:
        if s.count(_) == 1:
            return _