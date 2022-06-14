from typing import List
def say_hello(name: List[str], city, state):
    return "Hello, {}! Welcome to {}, {}!".format(' '.join(name), city, state)