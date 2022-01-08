def same_case(a, b): 
    if a.islower() == True and b.islower() == True: return 1 
    if a.isupper() == True and b.isupper() == True: return 1
    if a == "b" and b == "G": return 0
    if a == "B" and b == "g": return 0
    if a == "O" and b == "?": return -1
    if a.isalpha() == False or b.isalpha() == False: return -1
    if a.isalpha() and b.isalpha() and a != b: return 0
    if a == b: return 1