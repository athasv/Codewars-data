def take(arr,n):
    if not arr: return []
    if arr[0] is not None:
        return [arr[i] for i in range(len(arr)) if i < n]