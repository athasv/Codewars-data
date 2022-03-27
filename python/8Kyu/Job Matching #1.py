def match(candidate, job):
    #your code here
    return candidate["min_salary"] <= job["max_salary"] or candidate["min_salary"] <= (job["max_salary"] + (candidate["min_salary"]/100*10))