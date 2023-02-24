def map(function, *iterable):
    result = []
    if len(iterable) > 0:
        temp = min(len(subseq) for subseq in iterable)
        for i in range(temp):
            result.append(function(*[subseq[i] for subseq in iterable]))
    return result