import pygame

from rogue_hold.config import SPRITE_SHEET_PATH

pygame.init()
SPRITE_SHEET = pygame.image.load(SPRITE_SHEET_PATH)


def get_sprite(x: int, y: int, w: int, h: int, c: pygame.Color) -> pygame.Surface:
    sprite = SPRITE_SHEET.subsurface(pygame.Rect(x, y, w, h))
    sprite: pygame.Surface = sprite.convert()
    oc = sprite.map_rgb(pygame.Color(239, 239, 239))
    c = sprite.map_rgb(c)
    pixel_array = pygame.PixelArray(sprite)
    pixel_array.replace(oc, c)
    sprite = pixel_array.surface
    return sprite
