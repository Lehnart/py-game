from engine.esper import Processor
from engine.systems.rect.components import RectComponent, RectLimitComponent
from engine.systems.rect.events import MoveEvent


class RectProcessor(Processor):

    def __init__(self):
        pass

    def process(self, *args, **kwargs):
        move_events = self.world.receive(MoveEvent)
        for move_event in move_events:
            if not self.world.entity_exists(move_event.ent):
                continue

            if not self.world.has_component(move_event.ent, RectComponent):
                continue

            r = self.world.component_for_entity(move_event.ent, RectComponent)
            r.move(move_event.dx, move_event.dy)

            if not self.world.has_component(move_event.ent, RectLimitComponent):
                continue

            rect_limit = self.world.component_for_entity(move_event.ent, RectLimitComponent)
            r.x = max(r.x, rect_limit.x_min)
            r.x = min(r.x + r.w, rect_limit.x_max) - r.w
            r.y = max(r.y, rect_limit.y_min)
            r.y = min(r.y + r.h, rect_limit.y_max) - r.h
