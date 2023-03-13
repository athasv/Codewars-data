def content_weight(bottle_weight, scale): 
    if scale.split(" ")[2] == "larger":
        return bottle_weight - (bottle_weight/(int(scale.split(" ")[0])+1))
    elif scale.split(" ")[2] == "smaller":
        return bottle_weight/(int(scale.split(" ")[0])+1)