import datetime

import pygame

from engine.esper import Processor
from engine.systems.render.components import WindowComponent
from engine.systems.render.events import DrawRectSpriteEvent, DrawTextEvent, DrawSpriteEvent

FRAME_PER_SECONDS = 60


class RenderProcessor(Processor):

    def __init__(self):
        super().__init__()
        self.last_time_drawn = datetime.datetime.now()

    def process(self):

        if datetime.datetime.now() - self.last_time_drawn < datetime.timedelta(seconds=1. / FRAME_PER_SECONDS):
            return
        self.last_time_drawn = datetime.datetime.now()

        for window_entity, [window_component] in self.world.get_components(WindowComponent):
            self._draw_on_window(window_component)

    def _draw_on_window(self, window_component: WindowComponent):

        window_surface = window_component.surface()

        for rect_sprite_event in self.world.receive(DrawRectSpriteEvent):
            r, c = rect_sprite_event.rect, rect_sprite_event.c
            pygame.draw.rect(window_surface, c, pygame.Rect(r.x, r.y, r.w, r.h))

        for sprite_event in self.world.receive(DrawSpriteEvent):
            s, p = sprite_event.surf, sprite_event.pos
            window_surface.blit(s, p)

        for text_event in self.world.receive(DrawTextEvent):
            s, ft, c, pos = text_event.string, text_event.ft, text_event.c, text_event.pos
            txt_surf = ft.render(s, False, c)
            window_surface.blit(txt_surf, pos)

        pygame.display.flip()
        window_surface.fill((0, 0, 0))
