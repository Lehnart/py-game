from engine.esper import Event


class DecreaseLifeEvent(Event):

    def __init__(self):
        super().__init__()

class NewLifeValueEvent(Event):

    def __init__(self, life_value : int):
        super().__init__()
        self.life_value = life_value