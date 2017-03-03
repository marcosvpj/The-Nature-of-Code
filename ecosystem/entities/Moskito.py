import random
from random import randrange

import pygame

from ecosystem.entities.Entity import Entity
from vectors.PVector import PVector


class Moskito(Entity):
    def __init__(self):
        super().__init__()
        random.seed()
        self.location = PVector(randrange(50, 750), randrange(50, 550))
        self.velocity = PVector(2, 2)

    def update(self, screen):
        pygame.draw.circle(screen, (100, 100, 100), tuple(self.location), 2)

        random.seed()
        step = randrange(-1, 4)

        self.velocity = PVector(randrange(step-2, step+1), randrange(step-2, step+1))
        self.velocity *= 3

        self.location += self.velocity
