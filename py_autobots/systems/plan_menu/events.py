from engine.esper import Event


class NextPlanEvent(Event):

    def __init__(self, ent: int):
        super().__init__()
        self.ent = ent


class PreviousPlanEvent(Event):

    def __init__(self, ent: int):
        super().__init__()
        self.ent = ent
