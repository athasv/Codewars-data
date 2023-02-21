def warn_the_sheep(queue):
    pass
    for i in queue:
        if queue[len(queue) - 1] == "wolf": 
            return "Pls go away and stop eating my sheep"
    return "Oi! Sheep number {}! You are about to be eaten by a wolf!".format(len(queue) - (queue.index("wolf") + 1))