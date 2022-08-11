from engine.esper import Event


class TakeEvent(Event):

    def __init__(self, holder_ent: int, taken_ent: int):
        super().__init__()
        self.holder_ent = holder_ent
        self.taken_ent = taken_ent


class DropEvent(Event):

    def __init__(self, holder_ent: int):
        super().__init__()
        self.holder_ent = holder_ent
