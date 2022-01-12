from engine.esper import Event


class SetTextEvent(Event):

    def __init__(self, ent: int, txt: str):
        super().__init__()
        self.ent = ent
        self.txt = txt
