from engine.esper import Processor
from engine.systems.limit_rect.components import RectLimitComponent
from engine.systems.limit_rect.events import OutOfLimitEvent
from engine.systems.rect.events import HasMovedEvent


class LimitRectProcessor(Processor):

    def process(self, *args, **kwargs):

        has_moved_events = self.world.receive(HasMovedEvent)
        for has_moved_event in has_moved_events:
            if not self.world.entity_exists(has_moved_event.ent):
                continue

            if not self.world.has_component(has_moved_event.ent, RectLimitComponent):
                continue

            limit_comp = self.world.component_for_entity(has_moved_event.ent, RectLimitComponent)
            r = has_moved_event.r
            if r.x < limit_comp.x_min or r.x + r.w > limit_comp.x_max or r.y < limit_comp.y_min or r.y + r.h > limit_comp.y_max:
                pr = (r.x, r.y, r.w, r.h)

                r.x = max(r.x, limit_comp.x_min)
                r.x = min(r.x + r.w, limit_comp.x_max) - r.w
                r.y = max(r.y, limit_comp.y_min)
                r.y = min(r.y + r.h, limit_comp.y_max) - r.h

                self.world.publish(
                    OutOfLimitEvent(
                        has_moved_event.ent,
                        pr,
                        (r.x, r.y, r.w, r.h),
                        (limit_comp.x_min, limit_comp.x_max, limit_comp.y_min, limit_comp.y_max)
                    )
                )
