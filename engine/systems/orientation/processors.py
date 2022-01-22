from engine.esper import Processor
from engine.systems.orientation.components import OrientationComponent
from engine.systems.orientation.events import RotateEvent, HasRotatedEvent


class OrientationProcessor(Processor):

    def __init__(self):
        pass

    def process(self, *args, **kwargs):

        rotate_events = self.world.receive(RotateEvent)
        for rotate_event in rotate_events:

            if not self.world.entity_exists(rotate_event.ent):
                continue

            orientation_comp = self.world.try_component(rotate_event.ent, OrientationComponent)
            if orientation_comp is None:
                continue

            orientation_comp.angle += rotate_event.angle
            self.world.publish(HasRotatedEvent(rotate_event.ent, orientation_comp.angle))
