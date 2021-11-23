from typing import Tuple, List

import pygame

from engine.esper import World
from engine.systems.rectsprite.components import RectSpriteComponent


def get_rect_sprites(world: World) -> List[Tuple[pygame.Rect, pygame.Color]]:
    rect_sprites = world.get_component(RectSpriteComponent)
    return [(rect_sprite.rect, rect_sprite.color) for ent, rect_sprite in rect_sprites]
