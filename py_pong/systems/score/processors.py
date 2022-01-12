from engine.esper import Processor
from engine.systems.sprite_text.events import SetTextEvent
from py_pong.systems.score.components import ScoreComponent
from py_pong.systems.score.events import IncrementScoreEvent


class ScoreProcessor(Processor):

    def __init__(self):
        super().__init__()

    def process(self):

        for event in self.world.receive(IncrementScoreEvent):
            if not self.world.entity_exists(event.ent):
                continue

            if not self.world.has_component(event.ent, ScoreComponent):
                continue

            score_comp = self.world.component_for_entity(event.ent, ScoreComponent)
            score_comp.score += 1

            self.world.publish(SetTextEvent(event.ent, str(score_comp.score)))
