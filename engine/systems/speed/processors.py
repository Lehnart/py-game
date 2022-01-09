import datetime

from engine.esper import Processor
from engine.systems.speed.components import SpeedComponent
from engine.systems.speed.events import MoveEvent, InvertEvent


class SpeedProcessor(Processor):

    def __init__(self):
        self.last_process = datetime.datetime.now()

    def process(self, *args, **kwargs):
        invert_events = self.world.receive(InvertEvent)
        for invert_event in invert_events:
            if not self.world.entity_exists(invert_event.ent):
                continue

            if not self.world.has_component(invert_event.ent, SpeedComponent):
                continue

            speed_component = self.world.component_for_entity(invert_event.ent, SpeedComponent)
            if invert_event.invert_x :
                speed_component.vx *= -1

            if invert_event.invert_y:
                speed_component.vy *= -1

        dt = datetime.datetime.now() - self.last_process
        dt_seconds = dt.total_seconds()
        self.last_process = datetime.datetime.now()

        ents = self.world.get_component(SpeedComponent)
        for ent, rect_speed_component in ents:
            self.world.publish(
                MoveEvent(ent, rect_speed_component.vx * dt_seconds, rect_speed_component.vy * dt_seconds)
            )
