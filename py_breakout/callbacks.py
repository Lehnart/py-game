from engine import esper
from engine.esper import Event
from engine.systems.collision_rect.events import RectCollisionEvent
from engine.systems.destroyable.events import DestroyEvent
from engine.systems.limit_rect.events import OutOfLimitEvent
from engine.systems.sound.events import PlaySoundEvent
from engine.systems.speed.events import SetSpeedSignEvent, SetSpeedXEvent
from py_breakout.config import BALL_SPEED
from py_breakout.systems.score_value.events import SendScoreValueEvent


class BounceWallCallback:

    def __init__(self, ball_ent: int):
        self.ball = ball_ent

    def __call__(self, ent: int, out_of_limit_event: Event, world: esper.World):
        out_of_limit_event: OutOfLimitEvent
        if ent != out_of_limit_event.ent:
            return

        r = out_of_limit_event.r
        lims = out_of_limit_event.limits

        if r[0] < lims[0]:
            world.publish(SetSpeedSignEvent(ent, 1, 0))
            world.publish(PlaySoundEvent(self.ball))

        if r[0] + r[2] > lims[1]:
            world.publish(SetSpeedSignEvent(ent, -1, 0))
            world.publish(PlaySoundEvent(self.ball))

        if r[1] < lims[2]:
            world.publish(SetSpeedSignEvent(ent, 0, 1))
            world.publish(PlaySoundEvent(self.ball))

        if r[1] + r[3] > lims[3]:
            world.publish(SetSpeedSignEvent(ent, 0, -1))
            world.publish(PlaySoundEvent(self.ball))


class BounceRectCallback:

    def __init__(self, ball_ent: int, paddle_ent):
        self.ball = ball_ent
        self.paddle_ent = paddle_ent

    def __call__(self, ent: int, collision_event: Event, world: esper.World):
        collision_event: RectCollisionEvent
        if ent != collision_event.ent1 and ent != collision_event.ent2:
            return

        r_ball, r_paddle, rect_ent = (
            collision_event.rect1, collision_event.rect2, collision_event.ent2) \
            if ent == collision_event.ent1 \
            else (collision_event.rect2, collision_event.rect1, collision_event.ent1)

        if rect_ent == self.paddle_ent:
            xb = r_ball.x + (r_ball.w / 2)
            xp = r_paddle.x + (r_paddle.w / 2)
            rx = (xb - xp) / r_paddle.w
            world.publish(SetSpeedXEvent(ent, abs(BALL_SPEED[0]) * rx * 2.))

        world.publish(PlaySoundEvent(rect_ent))
        world.publish(DestroyEvent(rect_ent))
        world.publish(SendScoreValueEvent(rect_ent))

        if r_paddle.y < r_ball.y:
            world.publish(SetSpeedSignEvent(ent, 0, 1))
        else:
            world.publish(SetSpeedSignEvent(ent, 0, -1))
