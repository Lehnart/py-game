from typing import Tuple

from engine import esper
from engine.esper import Event
from engine.systems.collision_rect.events import RectCollisionEvent
from engine.systems.limit_rect.events import OutOfLimitEvent
from engine.systems.rect.events import SetPositionEvent
from engine.systems.sound.events import PlaySoundEvent
from engine.systems.speed.events import SetSpeedSignEvent, SetSpeedYEvent
from py_pong.config import BALL_RECT
from py_pong.systems.score.events import IncrementScoreEvent


class BounceWallCallback:

    def __init__(self, left_score_ent: int, right_score_ent: int, ball_ent: int):
        self.left = left_score_ent
        self.right = right_score_ent
        self.ball = ball_ent

    def __call__(self, ent: int, out_of_limit_event: Event, world: esper.World):
        out_of_limit_event: OutOfLimitEvent
        if ent != out_of_limit_event.ent:
            return

        r = out_of_limit_event.r
        lims = out_of_limit_event.limits

        if r[0] < lims[0]:
            world.publish(SetSpeedSignEvent(ent, 1, 0))
            world.publish(IncrementScoreEvent(self.left))
            world.publish(PlaySoundEvent(self.left))
            world.publish(SetPositionEvent(self.ball, BALL_RECT[0], BALL_RECT[1]))

        if r[0] + r[2] > lims[1]:
            world.publish(SetSpeedSignEvent(ent, -1, 0))
            world.publish(IncrementScoreEvent(self.right))
            world.publish(PlaySoundEvent(self.right))
            world.publish(SetPositionEvent(self.ball, BALL_RECT[0], BALL_RECT[1]))

        if r[1] < lims[2]:
            world.publish(SetSpeedSignEvent(ent, 0, 1))
            world.publish(PlaySoundEvent(ent))

        if r[1] + r[3] > lims[3]:
            world.publish(SetSpeedSignEvent(ent, 0, -1))
            world.publish(PlaySoundEvent(ent))


def bounce_paddle(ent: int, collision_event: Event, world: esper.World):
    collision_event: RectCollisionEvent
    if ent != collision_event.ent1 and ent != collision_event.ent2:
        return

    r_ball, r_paddle, paddle_ent = (
        collision_event.rect1, collision_event.rect2, collision_event.ent2) \
        if ent == collision_event.ent1 \
        else (collision_event.rect2, collision_event.rect1, collision_event.ent1)

    yb = r_ball.y + (r_ball.h / 2)
    yp = r_paddle.y + (r_paddle.h / 2)
    ry = (yb - yp) / r_paddle.h
    world.publish(SetSpeedYEvent(ent, 25. * ry * 2.))

    if r_paddle.x < r_ball.x:
        world.publish(SetSpeedSignEvent(ent, 1, 0))
        world.publish(PlaySoundEvent(paddle_ent))
    else:
        world.publish(SetSpeedSignEvent(ent, -1, 0))
        world.publish(PlaySoundEvent(paddle_ent))