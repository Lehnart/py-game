import math

from engine.esper import Event


class MoveEvent(Event):

    def __init__(self, ent: int, dx: float, dy: float):
        super().__init__()
        self.ent = ent
        self.dx = dx
        self.dy = dy


class SetSpeedSignEvent(Event):

    def __init__(self, ent: int, x_sign: int, y_sign: int):
        super().__init__()
        self.ent = ent
        self.x_sign = x_sign
        self.y_sign = y_sign


class SetSpeedOrientationEvent(Event):

    def __init__(self, ent: int, x: float, y: float):
        super().__init__()
        self.ent = ent
        self.fx = x / math.sqrt(x ** 2 + y ** 2)
        self.fy = y / math.sqrt(x ** 2 + y ** 2)


class SetSpeedYEvent(Event):

    def __init__(self, ent: int, y: float):
        super().__init__()
        self.ent = ent
        self.y = y


class SetSpeedXEvent(Event):

    def __init__(self, ent: int, x: float):
        super().__init__()
        self.ent = ent
        self.x = x