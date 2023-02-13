def multiple_of_index(arr):
    return [arr[i] for i,a in enumerate(range(len(arr))) if i != 0 if(arr[i]%i == 0 and i>0 and i!=0)]