from engine.esper import Processor
from engine.systems.render.events import DrawSpriteEvent, DrawTextEvent
from engine.systems.sprite.components import SpriteComponent
from engine.systems.sprite_text.components import TextSpriteComponent


class TextSpriteProcessor(Processor):

    def __init__(self):
        super().__init__()

    def process(self):

        for _, text_comp in self.world.get_component(TextSpriteComponent):
            self.world.publish(DrawTextEvent(text_comp.string, text_comp.ft, text_comp.color, text_comp.pos))
