def opposite(number):
    return number * (-1) if isinstance(number, int) or isinstance(number, float) and number > 0  else number * (-1)