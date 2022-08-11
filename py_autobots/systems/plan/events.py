from engine.esper import Event
from py_autobots.systems.ressource.components import Ressource


class CreatePlanEvent(Event):

    def __init__(self, plan_name: str, x: int, y: int):
        super().__init__()
        self.plan_name = plan_name
        self.x = x
        self.y = y


class AddRessourceEvent(Event):

    def __init__(self, dest_plan_ent: int, ressource: Ressource):
        super().__init__()
        self.dest_plan_ent = dest_plan_ent
        self.ressource = ressource
