from engine.esper import Event


class RotateEvent(Event):

    def __init__(self, ent: int, angle: float):
        super().__init__()
        self.ent = ent
        self.angle = angle

class HasRotatedEvent(Event):

    def __init__(self, ent: int, orientation_angle: float):
        super().__init__()
        self.ent = ent
        self.orientation_angle = orientation_angle
