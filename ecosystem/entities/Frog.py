import random
from random import randrange

import pygame

from ecosystem.entities.Entity import Entity
from ecosystem.entities.Moskito import Moskito
from vectors.PVector import PVector


class Frog(Entity):
    def __init__(self):
        super().__init__()
        random.seed()
        self.velocity = PVector(0, 0)

    def update(self, screen):
        random.seed()

        self.draw(screen)
        self.lock_target()

        move_chance = randrange(0, 10)
        if move_chance >= 7:
            self.velocity = PVector(randrange(-5, 5), randrange(-5, 5))

            if self.target_locked:
                self.direction = self.direction_to(self.target)
                self.velocity = self.direction

            self.velocity *= randrange(1, 3)
            self.location += self.velocity

    def draw(self, screen):
        self.location.x = int(self.location.x)
        self.location.y = int(self.location.y)
        pygame.draw.circle(screen, (150, 255, 150), tuple(self.location), 3)

    def lock_target(self):
        self.find_target(Moskito)
        self.target_locked = True
