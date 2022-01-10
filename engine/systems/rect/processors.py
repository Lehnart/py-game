import pygame

from engine.esper import Processor
from engine.systems.limit_rect.events import OutOfLimitEvent
from engine.systems.rect.components import RectComponent
from engine.systems.rect.events import HasMovedEvent
from engine.systems.speed.events import MoveEvent
from engine.systems.sprite_rect.events import SetRectSpritePosEvent


class RectProcessor(Processor):

    def process(self, *args, **kwargs):

        move_events = self.world.receive(MoveEvent)
        for move_event in move_events:
            if not self.world.entity_exists(move_event.ent):
                continue

            if not self.world.has_component(move_event.ent, RectComponent):
                continue

            r = self.world.component_for_entity(move_event.ent, RectComponent)
            previous_r = pygame.Rect(r.x, r.y, r.w, r.h)
            r.move(move_event.dx, move_event.dy)
            new_r = pygame.Rect(r.x, r.y, r.w, r.h)
            self.world.publish(HasMovedEvent(move_event.ent, previous_r, new_r))

        ool_events = self.world.receive(OutOfLimitEvent)
        for ool_event in ool_events:
            if not self.world.entity_exists(ool_event.ent):
                continue

            if not self.world.has_component(ool_event.ent, RectComponent):
                continue

            r = self.world.component_for_entity(ool_event.ent, RectComponent)
            r.set_position(ool_event.cr[0], ool_event.cr[1])

