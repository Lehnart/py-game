from engine.esper import Event


class CreatePlanEvent(Event):

    def __init__(self, plan_name: str, x: int, y: int):
        super().__init__()
        self.plan_name = plan_name
        self.x = x
        self.y = y
