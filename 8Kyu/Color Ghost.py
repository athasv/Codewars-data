import random

class Ghost(object):
    def __init__(self):
        colors = ['white', 'red', 'yellow', 'purple']
        self.color = random.choice(colors)