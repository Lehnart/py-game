from engine.esper import Processor
from engine.systems.render.events import DrawTextEvent
from engine.systems.sprite_string.components import StringSpriteComponent
from engine.systems.sprite_string.events import SetStringEvent, SetColorEvent

class StringSpriteProcessor(Processor):

    def __init__(self):
        super().__init__()

    def process(self):

        for event in self.world.receive(SetStringEvent):
            if not self.world.entity_exists(event.ent):
                continue

            if not self.world.has_component(event.ent, StringSpriteComponent):
                continue
            text_comp = self.world.component_for_entity(event.ent, StringSpriteComponent)
            text_comp.string = event.txt

        for event in self.world.receive(SetColorEvent):
            if not self.world.entity_exists(event.ent):
                continue

            if not self.world.has_component(event.ent, StringSpriteComponent):
                continue

            text_comp = self.world.component_for_entity(event.ent, StringSpriteComponent)
            text_comp.color = event.color

        for _, text_comp in self.world.get_component(StringSpriteComponent):
            self.world.publish(DrawTextEvent(text_comp.string, text_comp.ft, text_comp.color, text_comp.pos))
