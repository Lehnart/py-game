from engine.esper import Processor
from py_breakout.systems.score.events import AddScoreEvent
from py_breakout.systems.score_value.components import ScoreValueComponent
from py_breakout.systems.score_value.events import SendScoreValueEvent


class ScoreValueProcessor(Processor):

    def __init__(self):
        super().__init__()

    def process(self):

        for event in self.world.receive(SendScoreValueEvent):
            if not self.world.entity_exists(event.ent):
                continue

            if not self.world.has_component(event.ent, ScoreValueComponent):
                continue

            score_comp = self.world.component_for_entity(event.ent, ScoreValueComponent)
            self.world.publish(AddScoreEvent(score_comp.score_value))
