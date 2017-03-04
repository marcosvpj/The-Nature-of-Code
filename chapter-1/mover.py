from mover.Mover import Mover

import engine


class Loop:
    def __init__(self):
        self.mover = Mover()

    def loop(self, screen):
        screen.fill((0, 0, 0))
        self.mover.update(screen)


loop = Loop()
engine.main(loop.loop)
