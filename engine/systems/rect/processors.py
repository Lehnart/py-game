import datetime

from engine.esper import Processor
from engine.systems.rect.components import RectComponent, RectLimitComponent, RectSpeedComponent, RectBounceComponent
from engine.systems.rect.events import MoveEvent
from engine.systems.rectsprite.events import SetRectSpritePosEvent


class RectProcessor(Processor):

    def __init__(self):
        self.last_process = datetime.datetime.now()

    def process(self, *args, **kwargs):

        dt = datetime.datetime.now() - self.last_process
        dt_seconds = dt.total_seconds()
        self.last_process = datetime.datetime.now()

        ents = self.world.get_components(RectComponent, RectSpeedComponent)
        for ent, [_, rect_speed_component] in ents:
            self.world.publish(
                MoveEvent(ent, rect_speed_component.vx * dt_seconds, rect_speed_component.vy * dt_seconds))

        move_events = self.world.receive(MoveEvent)
        for move_event in move_events:
            if not self.world.entity_exists(move_event.ent):
                continue

            if not self.world.has_component(move_event.ent, RectComponent):
                continue

            r = self.world.component_for_entity(move_event.ent, RectComponent)
            r.move(move_event.dx, move_event.dy)

            if self.world.has_component(move_event.ent, RectLimitComponent):
                rect_limit = self.world.component_for_entity(move_event.ent, RectLimitComponent)

                if self.world.has_components(move_event.ent, RectBounceComponent, RectSpeedComponent):
                    rect_speed = self.world.component_for_entity(move_event.ent, RectSpeedComponent)
                    vx, vy = rect_speed.vx, rect_speed.vy
                    if r.x < rect_limit.x_min and vx < 0.:
                        rect_speed.vx *= -1
                    if r.x + r.w > rect_limit.x_max and vx > 0.:
                        rect_speed.vx *= -1
                    if r.y < rect_limit.y_min and vy < 0.:
                        rect_speed.vy *= -1
                    if r.y + r.h > rect_limit.y_max and vy > 0.:
                        rect_speed.vy *= -1

                r.x = max(r.x, rect_limit.x_min)
                r.x = min(r.x + r.w, rect_limit.x_max) - r.w
                r.y = max(r.y, rect_limit.y_min)
                r.y = min(r.y + r.h, rect_limit.y_max) - r.h

            self.world.publish(SetRectSpritePosEvent(move_event.ent, (int(r.x), int(r.y))))
