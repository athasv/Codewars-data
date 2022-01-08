def flip(text, arr):
    return sorted(arr) if text == 'R' else sorted(arr, reverse=True)