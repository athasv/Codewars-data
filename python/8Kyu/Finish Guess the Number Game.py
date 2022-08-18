class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self,n):
        if self.lives < 1: raise ValueError('Error!')
        if n != self.number:
            self.lives -= 1
            return False
        if n == self.number: return True