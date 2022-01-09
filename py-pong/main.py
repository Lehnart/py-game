import pygame

from engine.esper import World
from engine.systems.input.components import InputComponent
from engine.systems.input.processors import InputProcessor
from engine.systems.rect.components import RectComponent, RectLimitComponent, RectSpeedComponent, RectBounceComponent
from engine.systems.rect.events import MoveEvent
from engine.systems.rect.processors import RectProcessor
from engine.systems.rectsprite.components import RectSpriteComponent
from engine.systems.rectsprite.processors import RectSpriteProcessor
from engine.systems.render.components import WindowComponent
from engine.systems.render.processors import RenderProcessor
from engine.systems.sprite.components import SpriteComponent
from engine.systems.sprite.processors import SpriteProcessor
from engine.systems.textsprite.components import TextSpriteComponent
from engine.systems.textsprite.processors import TextSpriteProcessor

pygame.font.init()
PADDLE_SPEED = 500
SCORE_FONT = pygame.font.Font("res/atari.ttf", 96)


class PyPong(World):

    def __init__(self):
        super().__init__()
        self._is_running: bool = True

        # Window entity
        window = WindowComponent((800, 840))
        self.create_entity(window)

        # left paddle entity
        rect = RectComponent(5, 400, 20, 80)
        rect_limit = RectLimitComponent(0, 800, 0, 840)
        rect_sprite = RectSpriteComponent(pygame.Rect(5, 400, 20, 80), pygame.Color("white"))
        paddle1 = self.create_entity(rect, rect_limit, rect_sprite)

        self.add_component(
            paddle1,
            InputComponent(
                {
                    pygame.K_UP: lambda w: w.publish(MoveEvent(paddle1, 0, -w.process_dt * PADDLE_SPEED)),
                    pygame.K_DOWN: lambda w: w.publish(MoveEvent(paddle1, 0, +w.process_dt * PADDLE_SPEED)),
                }
            )
        )

        # Right paddle entity
        rect = RectComponent(775, 400, 20, 80)
        rect_limit = RectLimitComponent(0, 800, 0, 840)
        rect_sprite = RectSpriteComponent(pygame.Rect(775, 400, 20, 80), pygame.Color("white"))
        paddle2 = self.create_entity(rect, rect_limit, rect_sprite)
        self.add_component(
            paddle2,
            InputComponent(
                {
                    pygame.K_i: lambda w: w.publish(MoveEvent(paddle2, 0, -w.process_dt * PADDLE_SPEED)),
                    pygame.K_k: lambda w: w.publish(MoveEvent(paddle2, 0, +w.process_dt * PADDLE_SPEED)),
                }
            )
        )

        # center line
        center_line_surf = pygame.Surface((5, 840))
        h_segment = 10
        y0 = 0
        while y0 + h_segment < 840:
            pygame.draw.rect(center_line_surf, (255, 255, 255), (0, y0, 5, h_segment))
            y0 += 2 * h_segment
        sprite = SpriteComponent(398, 0, center_line_surf)
        self.create_entity(sprite)

        # ball
        rect = RectComponent(400, 420, 10, 10)
        rect_limit = RectLimitComponent(0, 800, 0, 840)
        rect_speed = RectSpeedComponent(200, 200)
        rect_bounce = RectBounceComponent()
        rect_sprite = RectSpriteComponent(pygame.Rect(400, 420, 10, 10), pygame.Color("white"))
        paddle2 = self.create_entity(rect, rect_limit, rect_sprite, rect_speed, rect_bounce)

        # left score
        left_score_text = TextSpriteComponent("0", SCORE_FONT, pygame.color.Color(255, 255, 255), (200, 0))
        left_score = self.create_entity(left_score_text)

        # right score
        right_score_text = TextSpriteComponent("0", SCORE_FONT, pygame.color.Color(255, 255, 255), (600, 0))
        right_score = self.create_entity(right_score_text)

        self.add_processor(RenderProcessor(), 1)
        self.add_processor(InputProcessor(), 2)
        self.add_processor(RectProcessor(), 3)
        self.add_processor(RectSpriteProcessor(), 4)
        self.add_processor(SpriteProcessor(), 5)
        self.add_processor(TextSpriteProcessor(), 6)

    def is_running(self) -> bool:
        return self._is_running


def run():
    game_world = PyPong()
    while game_world.is_running():
        game_world.process()


if __name__ == '__main__':
    # import cProfile
    # cProfile.run('run()', sort="cumtime")
    run()
