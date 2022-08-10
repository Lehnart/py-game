import pygame as pygame

pygame.font.init()
pygame.mixer.init()

TILE_SIZE = 32
TILE_COUNT = 25

WINDOW_SIZE = (1000, 800)

WINDOW_LIMITS = (0, 800, 0, 840)

HERO_RECT = (TILE_SIZE*12, TILE_SIZE*12, TILE_SIZE, TILE_SIZE)
WORKSHOP_RECT = (TILE_SIZE*18, TILE_SIZE*18, TILE_SIZE, TILE_SIZE)

HERO_SPRITE = pygame.image.load("res/hero_32.png")
GRASS_SPRITE = pygame.image.load("res/grass_32.png")
TREE_SPRITE = pygame.image.load("res/tree_32.png")
BRANCH_SPRITE = pygame.image.load("res/branch_32.png")
ROCK_SPRITE = pygame.image.load("res/rock_32.png")
WORKSHOP_SPRITE = pygame.image.load("res/workshop_32.png")



FRAME_RATE = 60

MENU_FONT_SIZE = 24
MENU_FONT = pygame.font.Font("res/atari.ttf", MENU_FONT_SIZE)
