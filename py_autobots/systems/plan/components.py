from typing import Dict

from py_autobots.systems.ressource.components import Ressource


class PlanComponent:
    def __init__(self, required_ressources: Dict[Ressource, int]):
        self.required_ressources = required_ressources

        self.current_ressources = {}
        for k in required_ressources:
            self.current_ressources[k] = 0
