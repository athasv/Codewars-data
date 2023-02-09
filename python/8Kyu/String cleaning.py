def string_clean(s):
    return "".join(_ for _ in s if not _.isdigit())