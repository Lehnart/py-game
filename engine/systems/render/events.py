from typing import Tuple

import pygame

from engine.esper import Event


class DrawRectSpriteEvent(Event):

    def __init__(self, rect: pygame.Rect, c: pygame.Color):
        super().__init__()
        self.rect = rect
        self.c = c


class DrawSpriteEvent(Event):

    def __init__(self, surf: pygame.Surface, pos: Tuple[int, int]):
        super().__init__()
        self.surf = surf
        self.pos = pos


class DrawTextEvent(Event):

    def __init__(self, string: str, ft: pygame.font.Font, c: pygame.Color, pos: Tuple[int, int]):
        super().__init__()
        self.string = string
        self.ft = ft
        self.c = c
        self.pos = pos
