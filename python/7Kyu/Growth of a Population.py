def nb_year(p0, percent, aug, p):
    num_of_years = 0
    while p0 < p:
        p0 = int(p0 + p0 * (percent * 0.01) + aug)
        num_of_years += 1
    return num_of_years