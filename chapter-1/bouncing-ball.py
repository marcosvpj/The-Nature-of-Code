import engine

from vectors.Ball import Ball


class Loop:
    def __init__(self):
        self.ball = Ball()

    def loop(self, screen):
        screen.fill((0, 0, 0))
        self.ball.update(screen)


loop = Loop()
engine.main(loop.loop)
