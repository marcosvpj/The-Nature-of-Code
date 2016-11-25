class PVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return PVector(self.x + other.x, self.y + other.y)

    def __iter__(self):
        return (self.x, self.y).__iter__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

