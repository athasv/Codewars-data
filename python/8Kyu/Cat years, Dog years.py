def human_years_cat_years_dog_years(human_years):
    
    def catYears(human_years):
            temp = {1:15, 2:24, 3:((human_years - 2) * 4)}
            if human_years == 1: return temp[1]
            if human_years == 2: return temp[2]
            if human_years >= 3: return temp[2] + temp[3]
            
    def dogYears(human_years):
            temp = {1:15, 2:24, 3:((human_years - 2) * 5)}
            if human_years == 1: return temp[1]
            if human_years == 2: return temp[2]
            if human_years >= 3: return temp[2] + temp[3]
# Your code here
    return [human_years,catYears(human_years),dogYears(human_years)]