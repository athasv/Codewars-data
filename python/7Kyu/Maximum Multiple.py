def max_multiple(divisor, bound):
    #your code here
    return max([_ for _ in range(bound+1) if _ % divisor == 0])