import random

from ecosystem.entities.Ant import Ant
from ecosystem.entities.Frog import Frog
from ecosystem.entities.Moskito import Moskito
from ecosystem.entities.Snail import Snail


class Loop:
    def __init__(self):
        self.entities = []
        self.create_entities(10)

    def create_entities(self, total):
        for x in range(0, total):
            specie = random.randrange(0, 100)
            if specie <= 35:
                self.entities.append(Ant())
            elif specie <= 70:
                self.entities.append(Moskito())
            elif specie <= 80:
                self.entities.append(Snail())
            elif specie <= 100:
                self.entities.append(Frog())

    def loop(self, screen):
        screen.fill((0, 0, 0))

        for entity in self.entities:
            entity.update(screen)

