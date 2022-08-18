def whoseMove(lastPlayer, win):
    if lastPlayer == 'black' and win == False: return 'white'
    if lastPlayer == 'white' and win == False: return 'black'
    if lastPlayer == 'black' and win == True: return 'black'
    if lastPlayer == 'white' and win == True: return 'white'