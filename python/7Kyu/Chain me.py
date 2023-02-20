def chain(init_val, functions):
    def add10(x):
        return x + 10

    def mul30(x):
        return x * 30
    
    for i in functions:
        init_val = i(init_val)
    return init_val