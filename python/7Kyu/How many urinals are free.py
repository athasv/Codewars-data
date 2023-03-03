def get_free_urinals(urinals):
    return -1 if  urinals.count("11") else urinals.replace("10", "1").replace("01","1").replace("00","0").count("0")