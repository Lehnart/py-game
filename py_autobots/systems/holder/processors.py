from engine.esper import Processor
from engine.systems.rect.components import RectComponent
from engine.systems.speed.events import MoveRectEvent
from engine.systems.sprite.events import FlipVisibilityEvent
from py_autobots.systems.holder.components import HolderComponent
from py_autobots.systems.holder.events import TakeEvent, DropEvent, RemoveEvent


class HolderProcessor(Processor):

    def __init__(self):
        super().__init__()

    def process(self):
        for event in self.world.receive(TakeEvent):
            if not self.world.entity_exists(event.holder_ent):
                continue

            if not self.world.entity_exists(event.taken_ent):
                continue

            if not self.world.has_component(event.holder_ent, HolderComponent):
                continue

            holder_component = self.world.component_for_entity(event.holder_ent, HolderComponent)

            if holder_component.hold_ent is not None:
                continue

            holder_component.hold_ent = event.taken_ent
            self.world.publish(FlipVisibilityEvent(event.taken_ent))
            print("taken ent "+ str(event.taken_ent))

        for event in self.world.receive(DropEvent):

            if not self.world.entity_exists(event.holder_ent):
                continue

            if not self.world.has_components(event.holder_ent, HolderComponent, RectComponent):
                continue

            holder_component = self.world.component_for_entity(event.holder_ent, HolderComponent)
            rect_component = self.world.component_for_entity(event.holder_ent, RectComponent)

            if holder_component.hold_ent is None:
                continue

            drop_ent = holder_component.hold_ent
            holder_component.hold_ent = None

            self.world.publish(FlipVisibilityEvent(drop_ent))
            if self.world.has_component(drop_ent, RectComponent):
                drop_rect_component = self.world.component_for_entity(drop_ent, RectComponent)
                self.world.publish(MoveRectEvent(drop_ent, rect_component.x - drop_rect_component.x, rect_component.y - drop_rect_component.y))


        for event in self.world.receive(RemoveEvent):

            if not self.world.entity_exists(event.holder_ent):
                continue

            if not self.world.has_components(event.holder_ent, HolderComponent, RectComponent):
                continue

            holder_component = self.world.component_for_entity(event.holder_ent, HolderComponent)
            holder_component.hold_ent = None