import random

import engine
from walker.CustomDistributionRandomWalker import CustomDistributionRandomWalker
from walker.GaussianRandomWalker import GaussianRandomWalker
from walker.NonUniformWalker import NonUniformWalker
from walker.RandomWalker import RandomWalker
from walker.WalkerSprite import WalkerSprite


class Loop:
    def __init__(self):
        self.walkerR = RandomWalker((700, 200))
        self.walkerRSprite = WalkerSprite(self.walkerR)

        self.walkerG = GaussianRandomWalker((300, 200))
        self.walkerGSprite = WalkerSprite(self.walkerG)

        self.walkerCD = CustomDistributionRandomWalker((100, 200))
        self.walkerCDSprite = WalkerSprite(self.walkerCD)

        self.walkerN = NonUniformWalker((700, 500))
        self.walkerNSprite = WalkerSprite(self.walkerN)

    def loop(self, screen):
        self.walkerRSprite.display(screen)
        self.walkerR.update()

        self.walkerNSprite.display(screen)
        self.walkerN.update()

        self.walkerGSprite.display(screen)
        self.walkerG.update()

        self.walkerCDSprite.display(screen)
        self.walkerCD.update()

        random.seed()


main_loop = Loop()

engine.main(main_loop.loop)
