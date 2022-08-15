def my_first_kata(a,b):
    if type(a) in (int, float, complex) and type(b) in (int, float, complex):
        return (a%b) + (b%a)
    if not isinstance(a, (int, float, complex)) or not isinstance(b, (int, float, complex)) or a == 0 or b == 0:
        return False
    if a == b in [True] or a == b in [False]:
        return False