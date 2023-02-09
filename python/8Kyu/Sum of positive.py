def positive_sum(arr):
    # Your code here
    temp = []
    for _ in arr:
        if _ > 0:
            temp.append(_)
    return sum(temp)
