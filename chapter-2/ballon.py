from random import randrange

import pygame

import engine
from vectors.PVector import PVector


class Balloon:
    def __init__(self):
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.location = PVector(randrange(50, 1000), 580)
        self.velocity_limit = False
        self.color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))

    def update(self, screen):

        helium = PVector(0, -1)
        self.acceleration += helium

        wind = PVector(randrange(-3, 5), randrange(-3, 0))
        self.acceleration += wind

        self.velocity += self.acceleration
        self.location += self.velocity
        self.acceleration *= 0

        if self.velocity_limit is not False:
            self.velocity.limit(self.velocity_limit)

        print(self.velocity.y)

        draw_position = (int(self.location.x), int(self.location.y))
        pygame.draw.circle(screen, self.color, draw_position, 10)

    def limit_velocity(self, limit):
        self.velocity_limit = limit


class Loop:
    def __init__(self):
        self.balloon = Balloon()

        self.balloon2 = Balloon()
        self.balloon2.limit_velocity(5)

    def loop(self, screen):
        screen.fill((0, 0, 0))

        self.balloon.update(screen)
        self.balloon2.update(screen)


main_loop = Loop()
engine.main(main_loop.loop, 15, screen_size=(1000,1000))
