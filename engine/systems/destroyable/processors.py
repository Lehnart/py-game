from engine.esper import Processor
from engine.systems.destroyable.components import DestroyableComponent
from engine.systems.destroyable.events import DestroyEvent


class DestroyableProcessor(Processor):

    def __init__(self):
        pass

    def process(self, *args, **kwargs):
        destroy_events = self.world.receive(DestroyEvent)
        for destroy_event in destroy_events:
            if not self.world.entity_exists(destroy_event.ent):
                continue

            if not self.world.has_component(destroy_event.ent, DestroyableComponent):
                continue

            self.world.delete_entity(destroy_event.ent, immediate=True)
