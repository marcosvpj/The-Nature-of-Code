import copy
from random import randrange

import pygame

import engine
from vectors.PVector import PVector
from noise import pnoise2, snoise2, pnoise1


class Balloon:
    def __init__(self):
        self.location = PVector(randrange(50, 750), 15)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)

        self.velocity_limit = False
        self.color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))

        self.mass = randrange(2, 10)

    def apply_force(self, force):
        self.acceleration += force / self.mass

    def update(self, screen):
        # helium = PVector(0, -1)
        # self.apply_force(helium)

        self.velocity += self.acceleration
        self.location += self.velocity
        self.acceleration *= 0

        if self.velocity_limit is not False:
            self.velocity.limit(self.velocity_limit)

        self.draw_on_screen(screen)
        self.bounce_on_edges()

    def limit_velocity(self, limit):
        self.velocity_limit = limit

    def draw_on_screen(self, screen):
        draw_position = (int(self.location.x), int(self.location.y))
        pygame.draw.circle(screen, self.color, draw_position, self.mass * 3)

    def bounce_on_edges(self):
        if self.location.y <= 10:
            self.location.y = 10
            self.velocity.y *= -1
        elif self.location.y >= 550:
            self.location.y = 550
            self.velocity.y *= -1

        if self.location.x <= 10:
            self.location.x = 10
            self.velocity.x *= -1
        elif self.location.x >= 790:
            self.location.x = 790
            self.velocity.x *= -1


class Loop:
    def __init__(self):
        self.entities = []
        for entity in range(5):
            self.entities.append(Balloon())

        self.t = randrange(0, 1000)
        self.base = 0
        self.points = 256
        self.span = 5.0
        self.octaves = 2

    def loop(self, screen):
        screen.fill((0, 0, 0))

        noise = self.calculate_noise()
        # noise *= 3

        for entity in self.entities:
            wind = PVector(noise, 0)
            entity.apply_force(wind)

            gravity = PVector(0, .5 * entity.mass)
            entity.apply_force(gravity)

            friction = self.calculate_friction(entity.velocity)
            entity.apply_force(friction)

            entity.update(screen)

    def calculate_friction(self, velocity):
        friction_coefficient = .5
        normal_force = 1
        friction_magnitude = friction_coefficient * normal_force

        friction = copy.deepcopy(velocity)
        friction *= -1
        friction.normalize()
        friction *= friction_magnitude

        return friction

    def calculate_noise(self):
        x = float(self.t) * self.span / self.points - 0.5 * self.span
        noise = pnoise1(x + self.base, self.octaves)
        self.t += 1
        return noise


main_loop = Loop()
engine.main(main_loop.loop, 15, screen_size=(800, 600))
