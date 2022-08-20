def evil(n):
    temp = bin(n).count('1')
    return "It's Evil!" if temp % 2 == 0 else "It's Odious!"