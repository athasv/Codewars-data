def capitalize_word(w):
    return "".join(c[:1].upper() + c[1:] for c in w.split(' '))