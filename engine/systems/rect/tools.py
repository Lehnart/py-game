from typing import Optional

import pygame

from engine.esper import World
from engine.systems.rect.components import RectComponent


def get_rect(world: World, ent: int) -> Optional[pygame.Rect]:
    if not world.entity_exists(ent):
        return None

    if not world.has_component(ent, RectComponent):
        return None

    return world.component_for_entity(ent, RectComponent)
