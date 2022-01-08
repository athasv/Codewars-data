def get_status(is_busy):
    temp = "available"
    if is_busy:
        temp = "busy"
    state = {"status" : temp}
    return state
