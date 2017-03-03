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
        self.location = PVector(randrange(200, 600), randrange(200, 600))
        self.direction = PVector(randrange(-1, 1), randrange(-1, 1))
        self.velocity = PVector(0, 0)
        self.target = PVector(randrange(100, 700), randrange(100, 500))
        self.target_locked = False

    def update(self, screen):
        self.location.x = int(self.location.x)
        self.location.y = int(self.location.y)
        pygame.draw.circle(screen, (150, 255, 150), tuple(self.location), 3)

        for entity in self.entities:
            if isinstance(entity, Moskito) and self.distance_to(entity.location) < self.distance_to(
                    self.target) and not self.target_locked:
                self.target = entity.location
        self.target_locked = True

        self.direction = self.direction_to(self.target)

        random.seed()

        move_chance = randrange(0, 10)
        if move_chance >= 7:
            self.velocity = PVector(randrange(-5, 5), randrange(-5, 5))
            self.velocity *= randrange(1, 3)
            self.velocity += self.direction
            self.location += self.velocity

    def direction_to(self, to):
        direction = to - self.location
        distance = self.distance_to(to)

        if distance / 10 > 0:
            direction /= distance / 10

        return direction
