import datetime

import pygame

from engine.esper import Processor
from engine.systems.rectsprite.tools import get_rect_sprites
from engine.systems.render.components import WindowComponent
from engine.systems.sprite.tools import get_sprites
from engine.systems.textsprite.tools import get_text_sprites

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

        rect_sprites = get_rect_sprites(self.world)
        for r, c in rect_sprites:
            pygame.draw.rect(window_surface, c, pygame.Rect(r.x, r.y, r.w, r.h))

        sprites = get_sprites(self.world)
        for p, s in sprites:
            window_surface.blit(s, p)

        text_sprites = get_text_sprites(self.world)
        for s, ft, c, pos in text_sprites:
            txt_surf = ft.render(s, False, c)
            window_surface.blit(txt_surf, pos)

        pygame.display.flip()
        window_surface.fill((0, 0, 0))
