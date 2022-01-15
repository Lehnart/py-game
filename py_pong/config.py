import pygame

pygame.font.init()
pygame.mixer.init()


def draw_center_line():
    s = pygame.Surface((5, 840))
    h_segment = 10
    y0 = 0
    while y0 + h_segment < 840:
        pygame.draw.rect(s, (255, 255, 255), (0, y0, 5, h_segment))
        y0 += 2 * h_segment
    return s


WINDOW_SIZE = (800, 840)
WINDOW_LIMITS = (0, 800, 0, 840)

PADDLE_LEFT_RECT = (5, 400, 20, 80)
PADDLE_RIGHT_RECT = (775, 400, 20, 80)
PADDLE_SPEED = 500

BALL_RECT = (380, 420, 10, 10)
BALL_SPEED = (-25,25)

CENTER_LINE_SPRITE = draw_center_line()

SCORE_LEFT_POS = (200,0)
SCORE_RIGHT_POS = (600,0)
SCORE_FONT = pygame.font.Font("res/atari.ttf", 96)

WALL_BOUNCE_SOUND = pygame.mixer.Sound("res/wall.wav")
PADDLE_BOUNCE_SOUND = pygame.mixer.Sound("res/racket.wav")
LOSE_SOUND = pygame.mixer.Sound("res/lose.wav")
