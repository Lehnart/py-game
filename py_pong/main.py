from engine.esper import World
from engine.systems.collision_rect.components import CollisionRectComponent
from engine.systems.collision_rect.events import RectCollisionEvent
from engine.systems.collision_rect.processors import CollisionRectProcessor
from engine.systems.event.components import EventComponent
from engine.systems.event.processors import EventProcessor
from engine.systems.input.components import InputComponent
from engine.systems.input.processors import InputProcessor
from engine.systems.limit_rect.components import RectLimitComponent
from engine.systems.limit_rect.events import OutOfLimitEvent
from engine.systems.limit_rect.processors import LimitRectProcessor
from engine.systems.rect.components import RectComponent
from engine.systems.rect.processors import RectProcessor
from engine.systems.render.components import WindowComponent
from engine.systems.render.processors import RenderProcessor
from engine.systems.sound.components import SoundComponent
from engine.systems.sound.processors import SoundProcessor
from engine.systems.speed.components import SpeedComponent
from engine.systems.speed.events import MoveEvent
from engine.systems.speed.processors import SpeedProcessor
from engine.systems.sprite.components import SpriteComponent
from engine.systems.sprite.processors import SpriteProcessor
from engine.systems.sprite_rect.components import RectSpriteComponent
from engine.systems.sprite_rect.processors import RectSpriteProcessor
from engine.systems.sprite_text.components import TextSpriteComponent
from engine.systems.sprite_text.processors import TextSpriteProcessor
from py_pong.callbacks import BounceWallCallback, bounce_paddle
from py_pong.config import *
from py_pong.systems.score.components import ScoreComponent
from py_pong.systems.score.processors import ScoreProcessor

class PyPong(World):

    def __init__(self):
        super().__init__()
        self._is_running: bool = True

        # Window entity
        window = WindowComponent(WINDOW_SIZE)
        self.create_entity(window)

        # left paddle entity
        rect = RectComponent(*PADDLE_LEFT_RECT)
        rect_collide = CollisionRectComponent(pygame.Rect(*PADDLE_LEFT_RECT))
        rect_limit = RectLimitComponent(*WINDOW_LIMITS)
        rect_sprite = RectSpriteComponent(pygame.Rect(*PADDLE_LEFT_RECT), pygame.Color("white"))
        bounce_sound = SoundComponent(PADDLE_BOUNCE_SOUND)
        paddle1 = self.create_entity(rect, rect_limit, rect_sprite, rect_collide, bounce_sound)

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
        rect = RectComponent(*PADDLE_RIGHT_RECT)
        rect_collide = CollisionRectComponent(pygame.Rect(*PADDLE_RIGHT_RECT))
        rect_limit = RectLimitComponent(*WINDOW_LIMITS)
        rect_sprite = RectSpriteComponent(pygame.Rect(*PADDLE_RIGHT_RECT), pygame.Color("white"))
        bounce_sound = SoundComponent(PADDLE_BOUNCE_SOUND)
        paddle2 = self.create_entity(rect, rect_limit, rect_sprite, rect_collide, bounce_sound)

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
        self.create_entity(SpriteComponent(400,0,CENTER_LINE_SPRITE))

        # left score
        left_score_text = TextSpriteComponent("0", SCORE_FONT, pygame.Color("white"), SCORE_LEFT_POS)
        left_score_comp = ScoreComponent(0)
        sound_comp = SoundComponent(LOSE_SOUND)
        left_score = self.create_entity(left_score_text, left_score_comp, sound_comp)

        # right score
        right_score_text = TextSpriteComponent("0", SCORE_FONT, pygame.Color("white"), SCORE_RIGHT_POS)
        right_score_comp = ScoreComponent(0)
        sound_comp = SoundComponent(LOSE_SOUND)
        right_score = self.create_entity(right_score_text, right_score_comp, sound_comp)

        # ball
        rect = RectComponent(*BALL_RECT)
        rect_collide = CollisionRectComponent(pygame.Rect(*BALL_RECT))
        rect_limit = RectLimitComponent(*WINDOW_LIMITS)
        rect_speed = SpeedComponent(*BALL_SPEED)
        rect_sprite = RectSpriteComponent(pygame.Rect(*BALL_RECT), pygame.Color("white"))
        bounce_sound = SoundComponent(WALL_BOUNCE_SOUND)
        ball = self.create_entity(rect, rect_limit, rect_sprite, rect_speed, rect_collide, bounce_sound)
        self.add_component(
            ball,
            EventComponent(
                {
                    OutOfLimitEvent: BounceWallCallback(left_score, right_score, ball),
                    RectCollisionEvent: bounce_paddle
                }
            )
        )

        self.add_processor(InputProcessor(), 20)
        self.add_processor(SpeedProcessor(), 19)
        self.add_processor(RectProcessor(), 18)
        self.add_processor(RectSpriteProcessor(), 17)
        self.add_processor(SpriteProcessor(), 16)
        self.add_processor(TextSpriteProcessor(), 15)
        self.add_processor(LimitRectProcessor(), 13)
        self.add_processor(CollisionRectProcessor(), 12)
        self.add_processor(EventProcessor(), 11)
        self.add_processor(ScoreProcessor(), 10)
        self.add_processor(RenderProcessor(FRAME_RATE), 9)
        self.add_processor(SoundProcessor(), 8)

    def is_running(self) -> bool:
        return self._is_running


def run():
    game_world = PyPong()
    while game_world.is_running():
        game_world.process()


if __name__ == '__main__':
    run()
