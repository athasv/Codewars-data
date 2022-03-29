def validate_usr(username):
    import re
    temp = re.compile(r"^[a-z0-9_]{4,16}$")
    return True if re.match(temp, username) else False