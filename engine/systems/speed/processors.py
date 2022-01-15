import datetime
import math

from engine.esper import Processor
from engine.systems.speed.components import SpeedComponent
from engine.systems.speed.events import MoveEvent, SetSpeedSignEvent, SetSpeedOrientationEvent, SetSpeedYEvent, \
    SetSpeedXEvent


class SpeedProcessor(Processor):

    def __init__(self):
        pass

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

        set_orientation_events = self.world.receive(SetSpeedOrientationEvent)
        for set_orientation_event in set_orientation_events:
            if not self.world.entity_exists(set_orientation_event.ent):
                continue

            if not self.world.has_component(set_orientation_event.ent, SpeedComponent):
                continue

            speed_component = self.world.component_for_entity(set_orientation_event.ent, SpeedComponent)
            mag = math.sqrt(speed_component.vx**2 + speed_component.vy ** 2)

            if speed_component.vx < 0. :
                speed_component.vx = -mag*set_orientation_event.fx
            else :
                speed_component.vx = mag * set_orientation_event.fx

            if speed_component.vy < 0.:
                speed_component.vy = -mag * set_orientation_event.fy
            else:
                speed_component.vy = mag * set_orientation_event.fy

        set_y_events = self.world.receive(SetSpeedYEvent)
        for set_y_event in set_y_events:
            if not self.world.entity_exists(set_y_event.ent):
                continue

            if not self.world.has_component(set_y_event.ent, SpeedComponent):
                continue

            speed_component = self.world.component_for_entity(set_y_event.ent, SpeedComponent)
            speed_component.vy = set_y_event.y

        set_x_events = self.world.receive(SetSpeedXEvent)
        for set_x_event in set_x_events:
            if not self.world.entity_exists(set_x_event.ent):
                continue

            if not self.world.has_component(set_x_event.ent, SpeedComponent):
                continue

            speed_component = self.world.component_for_entity(set_x_event.ent, SpeedComponent)
            speed_component.vx = set_x_event.x

        ents = self.world.get_component(SpeedComponent)
        for ent, rect_speed_component in ents:
            self.world.publish(
                MoveEvent(ent, rect_speed_component.vx * self.world.process_dt, rect_speed_component.vy * self.world.process_dt)
            )
