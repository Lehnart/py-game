from engine.esper import Event


class MoveEvent(Event):

    def __init__(self, ent: int, dx: float, dy: float):
        super().__init__()
        self.ent = ent
        self.dx = dx
        self.dy = dy
