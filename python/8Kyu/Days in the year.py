def year_days(year):
    return str(year) + " has 366 days" if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else str(year) + " has 365 days"