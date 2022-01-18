from engine.esper import Processor
from engine.systems.sprite_text.events import SetTextEvent
from py_breakout.systems.score.events import AddScoreEvent
from py_breakout.systems.score.components import ScoreComponent


class ScoreProcessor(Processor):

    def __init__(self):
        super().__init__()

    def process(self):

        for event in self.world.receive(AddScoreEvent):

            score_comps = self.world.get_component(ScoreComponent)
            for ent, score_comp in score_comps:
                score_comp.score += event.score
                self.world.publish(SetTextEvent(ent, str(score_comp.score)))
