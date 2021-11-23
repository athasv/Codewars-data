def are_you_playing_banjo(name:str) -> str:
    return "{} plays banjo".format(name) if name.startswith("R") or name.startswith("r") else "{} does not play banjo".format(name)
