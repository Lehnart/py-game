from engine.esper import Event


class MoveEvent(Event):

    def __init__(self, ent: int, dx: float, dy: float):
        super().__init__()
        self.ent = ent
        self.dx = dx
        self.dy = dy


class InvertEvent(Event):

    def __init__(self, ent: int, invert_x: bool, invert_y: bool):
        super().__init__()
        self.ent = ent
        self.invert_x = invert_x
        self.invert_y = invert_y
