from random import randrange
import random

import pygame

from vectors.PVector import PVector


class Frog:
    def __init__(self):
        random.seed()
        self.location = PVector(randrange(200, 600), randrange(200, 600))
        self.velocity = PVector(2, 2)
        self.direction = PVector(randrange(-1, 1), randrange(-1, 1))

    def update(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), tuple(self.location), 3)

        random.seed()

        move_chance = randrange(0, 10)
        if move_chance >= 9:
            self.velocity = PVector(randrange(-2, 3), randrange(-2, 3))
            self.velocity *= randrange(2, 4)

            self.location += self.velocity
