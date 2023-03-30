def countzero(string):
    #your code here
    if len(string) == 0: return 0
    if len(string) != 0: return sum(1 if c in "abdegopq069DOPQR" else 2 if c in "%&B8" else 0 for c in string.replace("()","0"))