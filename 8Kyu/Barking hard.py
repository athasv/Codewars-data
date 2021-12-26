class Dog:
    def __init__(self, breed: str):
        self.breed = breed
        self.bark = lambda: "Woof"

snoopy = Dog("Beagle")
scoobydoo = Dog("Great Dane")
