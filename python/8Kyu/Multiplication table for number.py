def multi_table(number):
    x = ""
    for _ in range(1,11):
        x = x + str(_) + " * " + str(number) + " = " + str(number*_) + "\n"
    return x.rstrip('\n')	