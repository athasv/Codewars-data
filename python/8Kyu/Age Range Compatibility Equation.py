def dating_range(age):
    return "{}-{}".format( int(age - (0.10*age)), int(age + (0.10*age))) if age <= 14 else "{}-{}".format(int((age/2) + 7), int((age-7)*2))