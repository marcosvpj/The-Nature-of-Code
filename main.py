import random

import engine
from Walker import Walker
from WalkerSprite import WalkerSprite

walker = Walker((500, 300))
walkerSprite = WalkerSprite(walker)

random.seed()

walker2 = Walker((200, 300))
walkerSprite2 = WalkerSprite(walker2)


def loop(screen):
    walkerSprite.display(screen)
    walker.update()

    walkerSprite2.display(screen)
    walker2.update()


engine.main(loop)
