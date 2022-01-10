from engine.esper import Processor
from engine.systems.rect.events import HasMovedEvent
from engine.systems.render.events import DrawRectSpriteEvent
from engine.systems.sprite_rect.components import RectSpriteComponent
from engine.systems.sprite_rect.events import SetRectSpritePosEvent


class RectSpriteProcessor(Processor):

    def __init__(self):
        pass

    def process(self, *args, **kwargs):

        has_moved_events = self.world.receive(HasMovedEvent)
        for has_moved_event in has_moved_events:

            if not self.world.entity_exists(has_moved_event.ent):
                continue

            rect_sprite_comp = self.world.try_component(has_moved_event.ent, RectSpriteComponent)
            if rect_sprite_comp is None:
                continue

            rect_sprite_comp.rect.x = has_moved_event.r[0]
            rect_sprite_comp.rect.y = has_moved_event.r[1]

        rect_sprites = self.world.get_component(RectSpriteComponent)
        for rect_ent, rect_comp in rect_sprites:
            self.world.publish(DrawRectSpriteEvent(rect_comp.rect, rect_comp.color))
