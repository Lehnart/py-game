from typing import Tuple, List

import pygame

from engine.esper import World
from engine.systems.textsprite.components import TextSpriteComponent


def get_text_sprites(world: World) -> List[Tuple[str, pygame.font.Font, pygame.Color, Tuple[int,int]]]:
    text_sprites = world.get_component(TextSpriteComponent)
    return [(text_sprite.string, text_sprite.ft, text_sprite.color, text_sprite.pos) for ent, text_sprite in text_sprites]
