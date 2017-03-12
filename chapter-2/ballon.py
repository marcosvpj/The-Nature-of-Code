import copy
from random import randrange

import pygame
from pygame.rect import Rect

import engine
from vectors.PVector import PVector
from noise import pnoise2, snoise2, pnoise1

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class Balloon:
    def __init__(self):
        self.location = PVector(randrange(50, 750), randrange(15, 100))
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
        elif self.location.y >= WINDOW_HEIGHT-50:
            self.location.y = WINDOW_HEIGHT-50
            self.velocity.y *= -1

        if self.location.x <= 10:
            self.location.x = 10
            self.velocity.x *= -1
        elif self.location.x >= WINDOW_WIDTH-50:
            self.location.x = WINDOW_WIDTH-50
            self.velocity.x *= -1

    def is_inside(self, liquid):
        if liquid.location.x < self.location.x < liquid.location.x + liquid.size[0]:
            if liquid.location.y < self.location.y < liquid.location.y + liquid.size[1]:
                return True
        return False

    def drag(self, liquid):
        speed = self.velocity.magnitude()
        drag_magnitude = liquid.coefficient * speed * speed

        drag = copy.deepcopy(self.velocity)
        drag *= -1
        drag.normalize()
        drag *= drag_magnitude

        self.apply_force(drag)


class Liquid:
    def __init__(self, position, size, coefficient):
        self.location = PVector(position[0], position[1])
        self.size = size
        self.coefficient = coefficient

    def update(self, screen):
        self.draw_on_screen(screen)

    def draw_on_screen(self, screen):
        area = Rect(tuple(self.location), self.size)
        pygame.draw.rect(screen, (10, 10, 10), area, 0)


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

        self.water = Liquid(coefficient=0.1, position=(0, WINDOW_HEIGHT / 2), size=(WINDOW_WIDTH, WINDOW_HEIGHT / 2))

    def loop(self, screen):
        screen.fill((0, 0, 0))

        self.water.update(screen)

        noise = self.calculate_noise()
        # noise *= 3

        for entity in self.entities:
            if entity.is_inside(self.water):
                entity.drag(self.water)

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
engine.main(main_loop.loop, 15, screen_size=(WINDOW_WIDTH, WINDOW_HEIGHT))
