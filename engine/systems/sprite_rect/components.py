import pygame.rect


class RectSpriteComponent:

    def __init__(self, rect: pygame.Rect, color: pygame.Color):
        self.rect = rect
        self.color = color

    def set_rect(self, r: pygame.Rect):
        self.rect = r
