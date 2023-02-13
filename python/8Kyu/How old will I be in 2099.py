def calculate_age(year_of_birth, current_year):
    if year_of_birth >  current_year and abs(year_of_birth - current_year) != 1: return "You will be born in {} years.".format(year_of_birth-current_year)
    if year_of_birth >  current_year and abs(year_of_birth - current_year) == 1: return "You will be born in {} year.".format(year_of_birth-current_year)
    if year_of_birth == current_year: return "{}".format("You were born this very year!") 
    if year_of_birth <  current_year and abs(year_of_birth - current_year) != 1: return "You are {} years old.".format(abs(year_of_birth-current_year))
    if year_of_birth <  current_year and abs(year_of_birth - current_year) == 1: return "You are {} year old.".format(abs(year_of_birth-current_year))