from random import randrange

import pygame


class Walker:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        s = pygame.Surface((2, 2))
        s.fill((100, 100, 100))

        self.sprite = s

    def display(self, surface):
        surface.blit(self.sprite, (self.x, self.y))

    def step(self):
        choice = randrange(0, 4)

        if choice == 0:
            self.x += 1
        if choice == 1:
            self.x -= 1
        if choice == 2:
            self.y += 1
        if choice == 3:
            self.y -= 1

    def update(self):
        self.step()
