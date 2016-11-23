import engine
from Walker import Walker

walker = Walker(400, 300)


def loop(screen):
    walker.display(screen)

    walker.update()
    pass


engine.main(loop)
