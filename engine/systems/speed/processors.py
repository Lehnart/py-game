import datetime

from engine.esper import Processor
from engine.systems.speed.components import SpeedComponent
from engine.systems.speed.events import MoveEvent, SetSpeedSignEvent


class SpeedProcessor(Processor):

    def __init__(self):
        self.last_process = datetime.datetime.now()

    def process(self, *args, **kwargs):
        set_sign_events = self.world.receive(SetSpeedSignEvent)
        for set_sign_event in set_sign_events:
            if not self.world.entity_exists(set_sign_event.ent):
                continue

            if not self.world.has_component(set_sign_event.ent, SpeedComponent):
                continue

            speed_component = self.world.component_for_entity(set_sign_event.ent, SpeedComponent)
            if set_sign_event.x_sign > 0:
                speed_component.vx = abs(speed_component.vx)
            if set_sign_event.x_sign < 0:
                speed_component.vx = -abs(speed_component.vx)

            if set_sign_event.y_sign > 0:
                speed_component.vy = abs(speed_component.vy)
            if set_sign_event.y_sign < 0:
                speed_component.vy = -abs(speed_component.vy)

        dt = datetime.datetime.now() - self.last_process
        dt_seconds = dt.total_seconds()

        self.last_process = datetime.datetime.now()

        ents = self.world.get_component(SpeedComponent)
        for ent, rect_speed_component in ents:
            self.world.publish(
                MoveEvent(ent, rect_speed_component.vx * dt_seconds, rect_speed_component.vy * dt_seconds)
            )
