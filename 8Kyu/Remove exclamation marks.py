def remove_exclamation_marks(s):
    #your code here
    output = "".join([x for x in s if x is not '!'])
    return output
            