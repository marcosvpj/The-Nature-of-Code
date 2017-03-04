from random import randrange

from walker.Walker import Walker


class NonUniformWalker(Walker):
    def step(self):
        direction = randrange(0, 10)

        if direction < 2:
            self.x += 1
        else:
            steps = randrange(-1, 1)
            self.x += steps

            steps = randrange(-1, 2)
            self.y += steps
