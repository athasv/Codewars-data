def alias_gen(f_name, l_name):
    if not f_name[0].isalpha(): return "Your name must start with a letter from A - Z."
    if not l_name[0].isalpha(): return "Your name must start with a letter from A - Z."
    F=f_name.capitalize()
    L=l_name.capitalize()
    return "{} {}".format(FIRST_NAME[F[0]], SURNAME[L[0]])
