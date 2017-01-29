from random import randrange

import pygame

from vectors.PVector import PVector


class Mover:
    def __init__(self):
        self.location = PVector(randrange(150, 300), randrange(150, 300))
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0.1, 0.01)
        self.top_speed = 1

    def step(self):
        self.velocity += self.acceleration
        self.velocity.limit(self.top_speed)
        self.location += self.velocity

    def check_edges(self, surface):
        if self.location.x > surface.get_width():
            self.location.x = 0
        elif self.location.x < 0:
            self.location.x = surface.get_width()

        if self.location.y > surface.get_height():
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = surface.get_height()

    def sprite(self):
        s = pygame.Surface((10, 10))
        s.fill((255, 255, 255))
        return s

    def update(self, surface):
        self.check_edges(surface)
        self.step()
        surface.blit(self.sprite(), tuple(self.location))
