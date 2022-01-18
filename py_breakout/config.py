import pygame

pygame.font.init()
pygame.mixer.init()

WINDOW_SIZE = (800, 840)
WINDOW_LIMITS = (0, 800, 0, 840)

PADDLE_RECT = (360, 750, 80, 20)
PADDLE_SPEED = 500

BALL_RECT = (380, 420, 10, 10)
BALL_SPEED = (-400, 400)

BLOCKS_N_COL = 14
BLOCKS_N_ROW = 6
BLOCKS_Y0 = 200
BLOCKS_H = 20
BLOCKS_H_STEP = 5
BLOCK_SCORE_VALUE_PER_ROW = [50, 50, 20, 20, 10, 10]

BLOCK_COLOR_PER_ROW = [pygame.Color("red"), pygame.Color("red"), pygame.Color("orange"), pygame.Color("orange"),
                       pygame.Color("green"), pygame.Color("green"), ]

LIVE_POS = (100, 0)
LIVE_FONT = pygame.font.Font("res/atari.ttf", 96)

SCORE_LEFT_POS = (100, 75)
SCORE_FONT = pygame.font.Font("res/atari.ttf", 96)

WALL_BOUNCE_SOUND = pygame.mixer.Sound("res/wall.wav")
PADDLE_BOUNCE_SOUND = pygame.mixer.Sound("res/racket.wav")
BLOCK_BOUNCE_SOUND = pygame.mixer.Sound("res/block.wav")
