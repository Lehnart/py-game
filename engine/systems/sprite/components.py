import pygame


class SpriteComponent:

    def __init__(self, x0: int, y0: int, sprite: pygame.Surface):
        self.x0 = x0
        self.y0 = y0
        self.sprite = sprite
        self.original_sprite = sprite
