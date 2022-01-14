from engine.esper import Event


class PlaySoundEvent(Event):

    def __init__(self, ent: int):
        super().__init__()
        self.ent = ent
