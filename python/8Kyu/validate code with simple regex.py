def validate_code(code):
    return True if int(str(code)[0]) in range(1, 4) else False