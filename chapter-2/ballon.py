from random import randrange

import pygame

import engine
from vectors.PVector import PVector
from noise import pnoise2, snoise2, pnoise1


class Balloon:
    def __init__(self):
        self.location = PVector(randrange(50, 750), 580)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)

        self.velocity_limit = False
        self.color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))

        self.mass = randrange(2, 5)

    def apply_force(self, force):
        force /= self.mass
        self.acceleration += force

    def update(self, screen):

        helium = PVector(0, -1)
        self.apply_force(helium)

        self.velocity += self.acceleration
        self.location += self.velocity
        self.acceleration *= 0

        if self.velocity_limit is not False:
            self.velocity.limit(self.velocity_limit)

        self.top_bounce()

        self.draw_on_screen(screen)

    def limit_velocity(self, limit):
        self.velocity_limit = limit

    def draw_on_screen(self, screen):
        draw_position = (int(self.location.x), int(self.location.y))
        pygame.draw.circle(screen, self.color, draw_position, 10)

    def top_bounce(self):
        if self.location.y <= 50:
            self.location.y = 50
            self.apply_force(self.velocity * self.mass * 3 * -1)


class Loop:
    def __init__(self):
        self.balloon = Balloon()
        self.balloon.limit_velocity(7)

        self.balloon2 = Balloon()
        self.balloon2.limit_velocity(5)

        self.t = randrange(0, 1000)
        self.base = 0
        self.points = 256
        self.span = 5.0
        self.octaves = 2

    def loop(self, screen):
        screen.fill((0, 0, 0))

        noise = self.calculate_noise()
        noise *= 10

        wind = PVector(noise, randrange(-3, 0))

        self.balloon.apply_force(wind)
        self.balloon2.apply_force(wind)

        self.balloon.update(screen)
        self.balloon2.update(screen)

    def calculate_noise(self):
        x = float(self.t) * self.span / self.points - 0.5 * self.span
        noise = pnoise1(x + self.base, self.octaves)
        self.t += 1
        return noise


main_loop = Loop()
engine.main(main_loop.loop, 15, screen_size=(800, 600))
