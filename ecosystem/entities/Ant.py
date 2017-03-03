import random
from random import randrange

import pygame

from ecosystem.entities.Entity import Entity
from vectors.PVector import PVector


class Ant(Entity):
    def __init__(self):
        super().__init__()
        random.seed()
        self.location = PVector(randrange(125, 150), randrange(125, 150))
        self.velocity = PVector(2, 2)

    def update(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), tuple(self.location), 1)

        leap_chance = randrange(0, 10)

        self.velocity = PVector(randrange(-1, 2), randrange(-1, 2))

        if leap_chance >= 5:
            self.velocity *= 2

        random.seed()

        self.location += self.velocity
