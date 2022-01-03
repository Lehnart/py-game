from typing import List, Tuple

import pygame

from engine.esper import World
from engine.systems.sprite.components import SpriteComponent


def get_sprites(world: World) -> List[Tuple[Tuple[int, int], pygame.Surface]]:
    sprite_comps = world.get_component(SpriteComponent)
    return [((sprite_comp.x0, sprite_comp.y0), sprite_comp.sprite) for ent, sprite_comp in sprite_comps]
