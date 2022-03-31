from datetime import datetime
def is_today(date): 
    return True if date.date() == datetime.date(datetime.today()) else False 