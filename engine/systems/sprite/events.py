from engine.esper import Event


class FlipVisibilityEvent(Event):

    def __init__(self, ent:int):
        self.ent = ent

