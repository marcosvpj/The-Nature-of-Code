from random import randrange

from vectors.PVector import PVector


class Entity:
    def __init__(self):
        self.location = PVector(randrange(200, 600), randrange(200, 600))
        self.entities = []
        self.direction = PVector(randrange(-1, 1), randrange(-1, 1))
        self.target = PVector(randrange(100, 700), randrange(100, 500))
        self.target_locked = False

    def setEntities(self, entities):
        self.entities = entities

    def distance_to(self, entity):
        if isinstance(entity, PVector):
            return (entity - self.location).magnitude()
        else:
            return (entity.location - self.location).magnitude()

    def direction_to(self, to):
        direction = to.location - self.location
        distance = self.distance_to(to.location)

        if distance / 10 > 0:
            direction /= distance / 10

        return direction

    def find_target(self, target):
        if self.target_locked:
            return False

        if self.closest_entity(target):
            self.target = self.closest_entity(target)

    def closest_entity(self, target):
        closest = False
        for entity in self.entities:
            if isinstance(entity, target) and closest is False:
                closest = entity

            if isinstance(entity, target) and self.distance_to(entity.location) < self.distance_to(closest.location):
                closest = entity

        return closest
