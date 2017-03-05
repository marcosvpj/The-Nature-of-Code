import math
from random import randrange


class PVector:
    def __init__(self, x, y) -> object:
        self.x = x
        self.y = y

    def x(self, x):
        self.x = x

    def y(self, y):
        self.y = y

    def __add__(self, other):
        return PVector(self.x + other.x, self.y + other.y)

    def __iter__(self):
        return (self.x, self.y).__iter__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __sub__(self, other):
        return PVector(self.x - other.x, self.y - other.y)

    def __mul__(self, n):
        return PVector(self.x * n, self.y * n)

    def magnitude(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def __truediv__(self, n):
        self.x = self.x / n
        self.y = self.y / n
        return self

    def normalize(self):
        if self.magnitude() != 0:
            self /= self.magnitude()

    def limit(self, limit):
        if self.magnitude() > limit:
            self.normalize()
            self.x *= limit
            self.y *= limit

    def random2D(self, limit):
        self.x = randrange(limit*-1, limit)
        self.y = randrange(limit*-1, limit)

