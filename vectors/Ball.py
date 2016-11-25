import pygame

from vectors.PVector import PVector


class Ball:
    def __init__(self):
        self.location = PVector(300, 150)
        self.velocity = PVector(2, 2)

    def update(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), tuple(self.location), 10)

        if self.is_inside_horizontal_boundaries(screen.get_width()):
            self.velocity.x *= -1

        if self.is_inside_vertical_boundaries(screen.get_height()):
            self.velocity.y *= -1

        self.location += self.velocity

    def is_inside_horizontal_boundaries(self, limit):
        return self.location.x + self.velocity.x > limit or self.location.x + self.velocity.x < 0

    def is_inside_vertical_boundaries(self, limit):
        return self.location.y + self.velocity.y > limit or self.location.y + self.velocity.y < 0
