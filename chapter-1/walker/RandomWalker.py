from random import randrange

from walker.Walker import Walker


class RandomWalker(Walker):
    def step(self):
        steps = randrange(-1, 2)
        self.x += steps

        steps = randrange(-1, 2)
        self.y += steps
