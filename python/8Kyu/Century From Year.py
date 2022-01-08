def century(year):
    temp = year // 100
    return temp + 1 if year % 100 != 0 else temp