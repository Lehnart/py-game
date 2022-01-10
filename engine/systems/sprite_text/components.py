from typing import Tuple

import pygame.font


class TextSpriteComponent:

    def __init__(self, string: str, ft: pygame.font.Font, color: pygame.Color, pos: Tuple[int, int]):
        self.string = string
        self.ft = ft
        self.color = color
        self.pos = pos
