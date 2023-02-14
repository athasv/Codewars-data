def is_digit(n):
    #your code here
    return True if bool(__import__("re").search('^[0-9]+$', n)) else False
	
def is_digit(n):
    #your code here
    return bool(__import__("re").fullmatch(r"(\d)", n))