def sum_of_differences(arr):
    arr = sorted(arr, reverse=True)
    for i in range(0,len(arr)):
        if len(arr) >0:
            sum = 0
            sum += abs(arr[i]-arr[i-1])
            return sum
    return 0
    