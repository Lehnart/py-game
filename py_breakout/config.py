import pygame

pygame.font.init()
pygame.mixer.init()

WINDOW_SIZE = (800, 840)
WINDOW_LIMITS = (0, 800, 0, 840)

PADDLE_RECT = (360, 750, 80, 20)
PADDLE_SPEED = 500

BALL_RECT = (380, 420, 10, 10)
BALL_SPEED = (-25,25)


SCORE_LEFT_POS = (200,0)
SCORE_FONT = pygame.font.Font("res/atari.ttf", 96)

WALL_BOUNCE_SOUND = pygame.mixer.Sound("res/wall.wav")
PADDLE_BOUNCE_SOUND = pygame.mixer.Sound("res/racket.wav")
BLOCK_BOUNCE_SOUND = pygame.mixer.Sound("res/block.wav")