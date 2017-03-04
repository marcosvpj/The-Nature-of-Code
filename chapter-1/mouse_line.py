import pygame

import engine
from vectors.PVector import PVector


class Loop:
    @staticmethod
    def loop(screen):
        screen.fill((0, 0, 0))

        center = PVector(screen.get_width() // 2, screen.get_height() // 2)
        mouse_position = PVector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        pygame.draw.line(screen, (255, 255, 255), tuple(center), tuple(mouse_position), 1)

        line = center - mouse_position
        s = pygame.Surface((line.magnitude(), 10))
        s.fill((255, 255, 255))
        screen.blit(s, (0, 0))


loop = Loop()
engine.main(loop.loop)
