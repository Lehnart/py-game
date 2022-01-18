from engine.esper import Event


class DecreaseLifeEvent(Event):

    def __init__(self):
        super().__init__()
