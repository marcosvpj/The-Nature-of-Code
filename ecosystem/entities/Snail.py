import random
from random import randrange

import pygame

from ecosystem.entities.Entity import Entity
from vectors.PVector import PVector


class Snail(Entity):
    def __init__(self):
        super().__init__()
        random.seed()
        self.location = PVector(randrange(200, 600), randrange(200, 600))
        self.velocity = PVector(2, 2)
        self.direction = PVector(randrange(-1, 1), randrange(-1, 1))

    def update(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), tuple(self.location), 2)

        leap_chance = randrange(0, 10)

        self.velocity = PVector(randrange(-1, 2), randrange(-1, 2))

        if leap_chance >= 5:
            self.velocity = self.direction

        random.seed()

        self.location += self.velocity
