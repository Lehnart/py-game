from engine.esper import Event


class AddScoreEvent(Event):

    def __init__(self, score: int):
        super().__init__()
        self.score = score
