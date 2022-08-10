from engine.esper import Event


class SelectPlanMenuItem(Event):

    def __init__(self, ent: int):
        super().__init__()
        self.ent = ent


class UnselectPlanMenuItem(Event):

    def __init__(self, ent: int):
        super().__init__()
        self.ent = ent
