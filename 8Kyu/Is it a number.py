def isDigit(string):
    #11ELF
    try:
        float(string) 
    except ValueError:
        try:
            complex(string)
        except ValueError:
            return False

    return True