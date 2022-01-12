from engine.esper import Processor
from engine.systems.render.events import DrawTextEvent
from engine.systems.sprite_text.components import TextSpriteComponent
from engine.systems.sprite_text.events import SetTextEvent


class TextSpriteProcessor(Processor):

    def __init__(self):
        super().__init__()

    def process(self):

        for event in self.world.receive(SetTextEvent):
            if not self.world.entity_exists(event.ent):
                continue

            if not self.world.has_component(event.ent, TextSpriteComponent):
                continue
            text_comp = self.world.component_for_entity(event.ent, TextSpriteComponent)
            text_comp.string = event.txt

        for _, text_comp in self.world.get_component(TextSpriteComponent):
            self.world.publish(DrawTextEvent(text_comp.string, text_comp.ft, text_comp.color, text_comp.pos))
