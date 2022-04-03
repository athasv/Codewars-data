def nba_extrap(ppg, mpg):
     return 0 if ppg == 0 else round(ppg * (48 / mpg), 1)