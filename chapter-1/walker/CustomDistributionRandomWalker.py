from random import randrange, seed

from walker.Walker import Walker


class CustomDistributionRandomWalker(Walker):
    def step(self):
        seed()

        step_size = randrange(-1, 4)
        step_x = randrange(step_size-2, step_size+1)
        step_size = randrange(-1, 4)
        step_y = randrange(step_size-2, step_size+1)

        self.x += step_x
        self.y += step_y
