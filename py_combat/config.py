import pygame

WINDOW_SIZE = (800, 840)
WINDOW_LIMITS = (0, 800, 0, 840)

TANK_LEFT_RECT = (100, 400, 27, 27)
TANK_SPEED = 50
TANK_ROTATION_SPEED = 1.
TANK_SPRITE = pygame.transform.scale(pygame.image.load("res/tank.bmp"), (27, 27))
