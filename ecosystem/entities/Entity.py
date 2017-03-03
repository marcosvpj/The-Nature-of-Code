class Entity:
    def __init__(self):
        self.entities = []

    def setEntities(self, entities):
        self.entities = entities

    def distance_to(self, entity):
        return (entity - self.location).magnitude()
