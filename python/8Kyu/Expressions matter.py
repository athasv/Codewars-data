def expression_matter(a, b, c):
    integers = [a, b, c]
    for i in integers:
        temp1 = a * b * c
        temp2 = (a + b) * c
        temp3 = a * (b + c)
        temp4 = a + b * c
        temp5 = a * b + c
        temp6 = a + b + c 
        a = [temp1, temp2, temp3, temp4, temp5, temp6]
        return max(a)