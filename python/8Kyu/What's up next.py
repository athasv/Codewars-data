def next_item(seq, item):
    seq = iter(seq)
    if item in seq:
        return next(seq, None)