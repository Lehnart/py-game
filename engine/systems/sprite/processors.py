import datetime

import pygame.transform

from engine.esper import Processor
from engine.systems.orientation.events import HasRotatedEvent
from engine.systems.rect.events import HasMovedEvent
from engine.systems.render.events import DrawSpriteEvent
from engine.systems.sprite.components import SpriteComponent


class SpriteProcessor(Processor):

    def __init__(self, frame_per_seconds: float = 60):
        super().__init__()
        self.frame_per_seconds = frame_per_seconds

    def process(self):

        has_moved_events = self.world.receive(HasMovedEvent)
        for has_moved_event in has_moved_events:

            if not self.world.entity_exists(has_moved_event.ent):
                continue

            sprite_comp = self.world.try_component(has_moved_event.ent, SpriteComponent)
            if sprite_comp is None:
                continue

            sprite_comp.x0 = has_moved_event.r[0]
            sprite_comp.y0 = has_moved_event.r[1]

        has_rotated_events = self.world.receive(HasRotatedEvent)
        for has_rotated_event in has_rotated_events:

            if not self.world.entity_exists(has_rotated_event.ent):
                continue

            sprite_comp = self.world.try_component(has_rotated_event.ent, SpriteComponent)
            if sprite_comp is None:
                continue

            print(has_rotated_event.orientation_angle)
            sprite_comp.sprite = pygame.transform.rotate(sprite_comp.original_sprite, has_rotated_event.orientation_angle)

        for _, sprite_comp in self.world.get_component(SpriteComponent):
            self.world.publish(DrawSpriteEvent(sprite_comp.sprite, (sprite_comp.x0, sprite_comp.y0)))
