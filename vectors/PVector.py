class PVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return PVector(self.x + other.x, self.y + other.y)

    def to_tuple(self):
        return self.x, self.y
