import engine
import pygame


class Ball:
    def __init__(self):
        self.x = 300
        self.y = 150

        self.yspeed = 2
        self.xspeed = 2

    def update(self, screen):
        pos = (self.x, self.y)
        pygame.draw.circle(screen, (255, 255, 255), pos, 10)

        if self.x + self.xspeed > screen.get_width():
            self.xspeed *= -1
        if self.x + self.xspeed < 0:
            self.xspeed *= -1

        if self.y + self.yspeed > screen.get_height():
            self.yspeed *= -1
        if self.y + self.yspeed < 0:
            self.yspeed *= -1

        self.x += self.xspeed
        self.y += self.yspeed


ball = Ball()


def loop(screen):
    screen.fill((0, 0, 0))
    ball.update(screen)


engine.main(loop)
