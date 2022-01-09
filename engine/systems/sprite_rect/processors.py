from engine.esper import Processor
from engine.systems.sprite_rect.components import RectSpriteComponent
from engine.systems.sprite_rect.events import SetRectSpritePosEvent
from engine.systems.render.events import DrawRectSpriteEvent


class RectSpriteProcessor(Processor):

    def __init__(self):
        pass

    def process(self, *args, **kwargs):

        set_pos_events = self.world.receive(SetRectSpritePosEvent)
        for set_pos_event in set_pos_events:

            if not self.world.entity_exists(set_pos_event.ent):
                continue

            rect_sprite_comp = self.world.try_component(set_pos_event.ent, RectSpriteComponent)
            if rect_sprite_comp is None:
                continue

            rect_sprite_comp.rect.x = set_pos_event.pos[0]
            rect_sprite_comp.rect.y = set_pos_event.pos[1]

        rect_sprites = self.world.get_component(RectSpriteComponent)
        for rect_ent, rect_comp in rect_sprites:
            self.world.publish(DrawRectSpriteEvent(rect_comp.rect, rect_comp.color))
