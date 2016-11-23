import random

import engine
from walker.GaussianRandomWalker import GaussianRandomWalker
from walker.NonUniformWalker import NonUniformWalker
from walker.RandomWalker import RandomWalker
from walker.WalkerSprite import WalkerSprite

walkerR = RandomWalker((700, 200))
walkerRSprite = WalkerSprite(walkerR)

random.seed()

walkerG = GaussianRandomWalker((300, 200))
walkerGSprite = WalkerSprite(walkerG)

random.seed()

walkerN = NonUniformWalker((700, 500))
walkerNSprite = WalkerSprite(walkerN)


def loop(screen):
    walkerRSprite.display(screen)
    walkerR.update()

    walkerNSprite.display(screen)
    walkerN.update()

    walkerGSprite.display(screen)
    walkerG.update()


engine.main(loop)
