from engine.esper import Processor
from engine.systems.event.components import EventComponent


class EventProcessor(Processor):

    def __init__(self):
        super().__init__()

    def process(self):

        event_components = self.world.get_component(EventComponent)
        for ent, event_component in event_components:
            event_classes = list(event_component.event_callbacks.keys())
            for ec in event_classes:
                events = self.world.receive(ec)
                for event in events:
                    event_component.event_callbacks[ec](ent, event, self.world)
