def basic_op(operator, value1, value2):
    result = {
      '+': lambda value1, value2: value1 + value2,
      '-': lambda value1, value2: value1 - value2,
      '*': lambda value1, value2: value1 * value2,
      '/': lambda value1, value2: value1 / value2
    }[operator](value1, value2)
    return result