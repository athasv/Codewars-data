class Sleigh(object):
    def authenticate(self, name, password):
        self.name = name
        self.password = password
        return True if (self.name == 'Santa Claus' and self.password == 'Ho Ho Ho!') else False