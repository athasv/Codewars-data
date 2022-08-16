def uefa_euro_2016(teams, scores):
    if scores[0] >  scores[1]: return "At match {} - {}, {} won!".format(teams[0], teams[1], teams[0])
    if scores[0] <  scores[1]: return "At match {} - {}, {} won!".format(teams[0], teams[1], teams[1])
    if scores[0] == scores[1]: return "At match {} - {}, {}".format(teams[0], teams[1], "teams played draw.")