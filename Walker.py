from abc import abstractmethod, ABCMeta


class Walker(metaclass=ABCMeta):
    def __init__(self, coord):
        self.x = coord[0]
        self.y = coord[1]

    def position(self):
        return self.x, self.y

    def update(self):
        self.step()

    @abstractmethod
    def step(self):
        pass
