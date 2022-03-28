def period_is_late(last,today,cycle_length):
    temp = today - last
    return True if temp.days > cycle_length else False