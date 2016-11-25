import pygame

from vectors.PVector import PVector


class Ball:
    def __init__(self):
        self.location = PVector(300, 150)

        self.velocity = PVector(2, 2)

    def update(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.location.to_tuple(), 10)

        if self.location.x + self.velocity.x > screen.get_width() or self.location.x + self.velocity.x < 0:
            self.velocity.x *= -1

        if self.location.y + self.velocity.y > screen.get_height() or self.location.y + self.velocity.y < 0:
            self.velocity.y *= -1

        self.location += self.velocity
