import random
from random import randrange

import pygame

from ecosystem.entities.Entity import Entity
import ecosystem
from vectors.PVector import PVector


class Moskito(Entity):
    def __init__(self):
        super().__init__()
        random.seed()
        self.location = PVector(randrange(50, 750), randrange(50, 550))
        self.velocity = PVector(2, 2)

    def update(self, screen):
        random.seed()

        self.draw(screen)
        self.find_target(ecosystem.entities.Frog.Frog)

        step = randrange(-1, 4)

        self.velocity = PVector(randrange(step - 2, step + 1), randrange(step - 2, step + 1))
        self.velocity *= 3

        if self.distance_to(self.target) < 100:
            self.velocity += self.direction_to(self.target) * -1
            self.velocity *= randrange(1, 2)

        self.location += self.velocity

    def draw(self, screen):
        self.location.x = int(self.location.x)
        self.location.y = int(self.location.y)
        pygame.draw.circle(screen, (100, 100, 100), tuple(self.location), 2)

