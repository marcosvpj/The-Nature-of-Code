import math


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

    def __sub__(self, other):
        return PVector(self.x - other.x, self.y - other.y)

    def magnitude(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def __truediv__(self, n):
        self.x = self.x / n
        self.y = self.y / n
        return self

    def normalize(self):
        return (self / self.magnitude()).magnitude()


