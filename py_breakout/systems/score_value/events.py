from engine.esper import Event


class SendScoreValueEvent(Event):

    def __init__(self, ent: int):
        super().__init__()
        self.ent = ent