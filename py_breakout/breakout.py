from engine.esper import World, Event
from engine.systems.collision_rect.components import CollisionRectComponent
from engine.systems.collision_rect.events import RectCollisionEvent
from engine.systems.collision_rect.processors import CollisionRectProcessor
from engine.systems.destroyable.components import DestroyableComponent
from engine.systems.destroyable.processors import DestroyableProcessor
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
from engine.systems.speed.events import MoveRectEvent
from engine.systems.speed.processors import SpeedProcessor
from engine.systems.sprite.processors import SpriteProcessor
from engine.systems.sprite_rect.components import RectSpriteComponent
from engine.systems.sprite_rect.processors import RectSpriteProcessor
from engine.systems.sprite_string.components import StringSpriteComponent
from engine.systems.sprite_string.processors import StringSpriteProcessor
from py_breakout.callbacks import BounceWallCallback, BounceRectCallback
from py_breakout.config import *
from py_breakout.systems.life.components import LifeComponent
from py_breakout.systems.life.events import NewLifeValueEvent
from py_breakout.systems.life.processors import LifeProcessor
from py_breakout.systems.score.components import ScoreComponent
from py_breakout.systems.score.processors import ScoreProcessor
from py_breakout.systems.score_value.components import ScoreValueComponent
from py_breakout.systems.score_value.processors import ScoreValueProcessor

def reset(ent:int, event:Event, world:World):
    event : NewLifeValueEvent
    if event.life_value == 0 :
        world.delete_entities()
        world.init_entities()

class PyBreakout(World):

    def __init__(self):
        super().__init__()
        self._is_running: bool = True

        # Window entity
        window = WindowComponent(WINDOW_SIZE)
        reset_comp = EventComponent(
            {
                NewLifeValueEvent:reset,
            }
        )
        self.create_entity(window, reset_comp)
        self.init_entities()

        self.add_processor(InputProcessor(), 20)
        self.add_processor(SpeedProcessor(), 19)
        self.add_processor(RectProcessor(), 18)
        self.add_processor(RectSpriteProcessor(), 17)
        self.add_processor(SpriteProcessor(), 16)
        self.add_processor(StringSpriteProcessor(), 15)
        self.add_processor(LimitRectProcessor(), 13)
        self.add_processor(CollisionRectProcessor(), 12)
        self.add_processor(EventProcessor(), 11)
        self.add_processor(RenderProcessor(FRAME_RATE), 9)
        self.add_processor(SoundProcessor(), 8)
        self.add_processor(ScoreValueProcessor(), 7)
        self.add_processor(ScoreProcessor(), 6)
        self.add_processor(LifeProcessor(), 5)

        self.add_processor(DestroyableProcessor(), 0)

    def delete_entities(self):
        for block in self.blocks:
            if self.entity_exists(block) :
                self.delete_entity(block, True)

        self.delete_entity(self.paddle, True)
        self.delete_entity(self.lives, True)
        self.delete_entity(self.ball, True)
        self.delete_entity(self.score, True)

    def init_entities(self):

        # Blocks
        self.blocks = []
        ww, wh = WINDOW_SIZE
        y = BLOCKS_Y0
        for j in range(BLOCKS_N_ROW):
            x = 0
            for i in range(BLOCKS_N_COL):
                rect = RectComponent(x, y, ww / BLOCKS_N_COL * 0.9, BLOCKS_H)
                rect_collide = CollisionRectComponent(pygame.Rect(x, y, ww / BLOCKS_N_COL * 0.9, BLOCKS_H))
                rect_sprite = RectSpriteComponent(pygame.Rect(x, y, ww / BLOCKS_N_COL * 0.9, BLOCKS_H),
                                                  BLOCK_COLOR_PER_ROW[j])
                score_value = ScoreValueComponent(BLOCK_SCORE_VALUE_PER_ROW[j])

                bounce_sound = SoundComponent(BLOCK_BOUNCE_SOUND)
                block = self.create_entity(rect, rect_sprite, rect_collide, bounce_sound, DestroyableComponent(),
                                           score_value)
                self.blocks.append(block)
                x += ww / BLOCKS_N_COL
            y += BLOCKS_H + BLOCKS_H_STEP

        # paddle entity
        rect = RectComponent(*PADDLE_RECT)
        rect_collide = CollisionRectComponent(pygame.Rect(*PADDLE_RECT))
        rect_limit = RectLimitComponent(*WINDOW_LIMITS)
        rect_sprite = RectSpriteComponent(pygame.Rect(*PADDLE_RECT), pygame.Color("white"))
        bounce_sound = SoundComponent(PADDLE_BOUNCE_SOUND)
        self.paddle = self.create_entity(rect, rect_limit, rect_sprite, rect_collide, bounce_sound)

        self.add_component(
            self.paddle,
            InputComponent(
                {
                    pygame.K_LEFT: lambda w: w.publish(MoveRectEvent(self.paddle, -w.process_dt * PADDLE_SPEED, 0.)),
                    pygame.K_RIGHT: lambda w: w.publish(MoveRectEvent(self.paddle, +w.process_dt * PADDLE_SPEED, 0.)),
                }
            )
        )

        # score
        left_score_text = StringSpriteComponent("0", SCORE_FONT, pygame.Color("white"), SCORE_LEFT_POS)
        score_comp = ScoreComponent(0)
        self.score = self.create_entity(left_score_text, score_comp)

        # lives
        lives_text = StringSpriteComponent("3", SCORE_FONT, pygame.Color("white"), LIVE_POS)
        life = LifeComponent(3)
        self.lives = self.create_entity(lives_text, life)

        # ball
        rect = RectComponent(*BALL_RECT)
        rect_collide = CollisionRectComponent(pygame.Rect(*BALL_RECT))
        rect_limit = RectLimitComponent(*WINDOW_LIMITS)
        rect_speed = SpeedComponent(*BALL_SPEED)
        rect_sprite = RectSpriteComponent(pygame.Rect(*BALL_RECT), pygame.Color("white"))
        bounce_sound = SoundComponent(WALL_BOUNCE_SOUND)
        self.ball = self.create_entity(rect, rect_limit, rect_sprite, rect_speed, rect_collide, bounce_sound)
        self.add_component(
            self.ball,
            EventComponent(
                {
                    OutOfLimitEvent: BounceWallCallback(self.ball, BALL_RECT[:2]),
                    RectCollisionEvent: BounceRectCallback(self.ball, self.paddle)
                }
            )
        )

    def is_running(self) -> bool:
        return self._is_running


def run():
    game_world = PyBreakout()
    while game_world.is_running():
        game_world.process()


if __name__ == '__main__':
    run()
