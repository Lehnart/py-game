from enum import Enum


class Ressource(Enum):
    WOOD = 1,
    BRANCH = 2,
    STONE = 3,


class RessourceComponent:

    def __init__(self, res: Ressource):
        self.res = res
