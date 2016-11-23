from random import randrange, gauss
from time import sleep

from walker.Walker import Walker


class GaussianRandomWalker(Walker):
    def step(self):
        steps = randrange(-1, 2)
        self.x += steps * gauss(2, 1)

        steps = randrange(-1, 2)
        self.y += steps * gauss(2, 1)
