def shortcut( s ):
    temp = [char for char in s if char not in "aeiou"]
    return "".join(temp)