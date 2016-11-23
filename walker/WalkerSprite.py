from random import randrange

import pygame


class WalkerSprite:
    def __init__(self, walker):
        self.walker = walker
        self.color = self.set_color()

    def sprite(self):
        s = pygame.Surface((1, 1))
        s.fill(self.color)
        return s

    def display(self, surface):
        surface.blit(self.sprite(), self.walker.position())

    def set_color(self):
        return randrange(0, 255), randrange(0, 255), randrange(0, 255)