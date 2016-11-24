import random

import engine
from walker.CustomDistributionRandomWalker import CustomDistributionRandomWalker
from walker.GaussianRandomWalker import GaussianRandomWalker
from walker.NonUniformWalker import NonUniformWalker
from walker.RandomWalker import RandomWalker
from walker.WalkerSprite import WalkerSprite

walkerR = RandomWalker((700, 200))
walkerRSprite = WalkerSprite(walkerR)

walkerG = GaussianRandomWalker((300, 200))
walkerGSprite = WalkerSprite(walkerG)

walkerCD = CustomDistributionRandomWalker((100, 200))
walkerCDSprite = WalkerSprite(walkerCD)

walkerN = NonUniformWalker((700, 500))
walkerNSprite = WalkerSprite(walkerN)


def loop(screen):
    walkerRSprite.display(screen)
    walkerR.update()

    walkerNSprite.display(screen)
    walkerN.update()

    walkerGSprite.display(screen)
    walkerG.update()

    walkerCDSprite.display(screen)
    walkerCD.update()

    random.seed()


engine.main(loop)
