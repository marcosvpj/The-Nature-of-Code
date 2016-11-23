from random import randrange


class Walker:
    def __init__(self, coord):
        self.x = coord[0]
        self.y = coord[1]

    def step(self):
        steps = randrange(-1, 2)
        self.x += steps

        steps = randrange(-1, 2)
        self.y += steps

    def update(self):
        self.step()

    def position(self):
        return self.x, self.y

