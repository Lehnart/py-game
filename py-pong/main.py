import pygame

from engine import esper
from engine.esper import World, Event
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
from engine.systems.speed.components import SpeedComponent
from engine.systems.speed.events import MoveEvent, InvertEvent
from engine.systems.speed.processors import SpeedProcessor
from engine.systems.sprite.components import SpriteComponent
from engine.systems.sprite.processors import SpriteProcessor
from engine.systems.sprite_rect.components import RectSpriteComponent
from engine.systems.sprite_rect.processors import RectSpriteProcessor
from engine.systems.sprite_text.components import TextSpriteComponent
from engine.systems.sprite_text.processors import TextSpriteProcessor

pygame.font.init()
PADDLE_SPEED = 500
SCORE_FONT = pygame.font.Font("res/atari.ttf", 96)


def bounce_paddle(ent: int, collision_event: Event, world: esper.World):
    collision_event: RectCollisionEvent
    if ent != collision_event.ent1 and ent != collision_event.ent2:
        return
    world.publish(InvertEvent(ent, True, False))

    r_ball, r_paddle = (collision_event.rect1, collision_event.rect2) if ent == collision_event.ent1 else (
        collision_event.rect2, collision_event.rect1)

    if r_paddle.x < r_ball.x:
        world.publish(MoveEvent(ent, r_paddle.x + r_paddle.w - r_ball.x, 0))
    else:
        world.publish(MoveEvent(ent, r_paddle.x - (r_ball.x + r_ball.w), 0))

def bounce_wall(ent: int, out_of_limit_event: Event, world: esper.World):
    out_of_limit_event: OutOfLimitEvent
    if ent != out_of_limit_event.ent:
        return

    r = out_of_limit_event.r
    lims = out_of_limit_event.limits

    if r[0] < lims[0]:
        world.publish(InvertEvent(ent, True, False))
    if r[0] + r[2] > lims[1]:
        world.publish(InvertEvent(ent, True, False))
    if r[1] < lims[2]:
        world.publish(InvertEvent(ent, False, True))
    if r[1] + r[3] > lims[3]:
        world.publish(InvertEvent(ent, False, True))


class PyPong(World):

    def __init__(self):
        super().__init__()
        self._is_running: bool = True

        # Window entity
        window = WindowComponent((800, 840))
        self.create_entity(window)

        # left paddle entity
        rect = RectComponent(5, 400, 20, 80)
        rect_collide = CollisionRectComponent(pygame.Rect(5, 400, 20, 80))
        rect_limit = RectLimitComponent(0, 800, 0, 840)
        rect_sprite = RectSpriteComponent(pygame.Rect(5, 400, 20, 80), pygame.Color("white"))
        paddle1 = self.create_entity(rect, rect_limit, rect_sprite, rect_collide)

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
        rect_collide = CollisionRectComponent(pygame.Rect(775, 400, 20, 80))
        rect_limit = RectLimitComponent(0, 800, 0, 840)
        rect_sprite = RectSpriteComponent(pygame.Rect(775, 400, 20, 80), pygame.Color("white"))
        paddle2 = self.create_entity(rect, rect_limit, rect_sprite, rect_collide)
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
        rect = RectComponent(380, 420, 10, 10)
        rect_collide = CollisionRectComponent(pygame.Rect(400, 420, 10, 10))
        rect_limit = RectLimitComponent(0, 800, 0, 840)
        rect_speed = SpeedComponent(-300, 300)
        rect_sprite = RectSpriteComponent(pygame.Rect(400, 420, 10, 10), pygame.Color("white"))
        bounce_comp = EventComponent({OutOfLimitEvent: bounce_wall, RectCollisionEvent: bounce_paddle})
        paddle2 = self.create_entity(rect, rect_limit, rect_sprite, rect_speed, rect_collide, bounce_comp)

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
        self.add_processor(EventProcessor(), 7)
        self.add_processor(SpeedProcessor(), 8)
        self.add_processor(LimitRectProcessor(), 9)
        self.add_processor(CollisionRectProcessor(), 10)

    def is_running(self) -> bool:
        return self._is_running


def run():
    game_world = PyPong()
    while game_world.is_running():
        game_world.process()


if __name__ == '__main__':
    run()
