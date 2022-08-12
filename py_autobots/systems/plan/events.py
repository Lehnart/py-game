from engine.esper import Event
from py_autobots.systems.ressource.components import Ressource


class CreatePlanEvent(Event):

    def __init__(self, plan_name: str, x: int, y: int):
        super().__init__()
        self.plan_name = plan_name
        self.x = x
        self.y = y


class AddRessourceEvent(Event):

    def __init__(self, dest_plan_ent: int, res_ent: int, holder_ent : int):
        super().__init__()
        self.dest_plan_ent = dest_plan_ent
        self.res_ent = res_ent
        self.holder_ent = holder_ent

class BuildEvent(Event):

    def __init__(self, dest_plan_ent: int):
        super().__init__()
        self.dest_plan_ent = dest_plan_ent
