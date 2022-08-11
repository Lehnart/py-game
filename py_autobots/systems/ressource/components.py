from enum import Enum


class Ressource(Enum):
    WOOD = 1,
    STONE = 2,


class RessourceComponent:

    def __init__(self, res: Ressource):
        self.res = res
