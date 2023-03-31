def adjacent_element_product(array):
    if len(array) >= 2:
        return max (_*__ for _, __ in zip(array, array[1:]))