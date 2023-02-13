def pillars(num_pill, dist, width):
    pass
    if num_pill < 2: return 0
    if num_pill == 2: return dist * 100
    if num_pill > 2:   return ( (num_pill-1) * dist) * 100  + (num_pill - 2) * width