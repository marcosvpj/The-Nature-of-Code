import random

import engine
from NonUniformWalker import NonUniformWalker
from RandomWalker import RandomWalker
from WalkerSprite import WalkerSprite

walkerR = RandomWalker((700, 300))
walkerRSprite = WalkerSprite(walkerR)

random.seed()

walkerN = NonUniformWalker((400, 300))
walkerNSprite = WalkerSprite(walkerN)


def loop(screen):
    walkerRSprite.display(screen)
    walkerR.update()

    walkerNSprite.display(screen)
    walkerN.update()


engine.main(loop)
