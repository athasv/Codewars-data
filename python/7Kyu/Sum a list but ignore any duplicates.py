def sum_no_duplicates(lst):
    return sum(x for x in set(lst) if lst.count(x) < 2)