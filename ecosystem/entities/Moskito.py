from random import randrange
import random

import pygame

from vectors.PVector import PVector


class Moskito:
    def __init__(self):
        random.seed()
        self.location = PVector(randrange(50, 750), randrange(50, 550))
        self.velocity = PVector(2, 2)

    def update(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), tuple(self.location), 2)

        random.seed()
        step = randrange(-1, 4)

        self.velocity = PVector(randrange(step-2, step+1), randrange(step-2, step+1))
        self.velocity *= 3

        self.location += self.velocity
