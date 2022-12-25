def replace_exclamation(s):
    return "".join("!" if _.lower() in "aeiou" else _ for _ in s)