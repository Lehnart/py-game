from engine.esper import Processor
from engine.systems.collision_rect.components import CollisionRectComponent
from engine.systems.collision_rect.events import RectCollisionEvent
from engine.systems.rect.events import HasMovedEvent


class CollisionRectProcessor(Processor):

    def __init__(self):
        pass

    def process(self, *args, **kwargs):

        has_moved_events = self.world.receive(HasMovedEvent)
        for has_moved_event in has_moved_events:
            if not self.world.entity_exists(has_moved_event.ent):
                continue

            if not self.world.has_component(has_moved_event.ent, CollisionRectComponent):
                continue

            collision_rect_comp = self.world.component_for_entity(has_moved_event.ent, CollisionRectComponent)
            collision_rect_comp.rect.x, collision_rect_comp.rect.y = has_moved_event.r.x, has_moved_event.r.y

        collision_rects = self.world.get_component(CollisionRectComponent)
        rects = [cr.rect for _, cr in collision_rects]

        current_index = 0
        for ent, cr in collision_rects:
            collisions = cr.rect.collidelistall(rects[current_index+1:])
            for i in collisions:
                self.world.publish(
                    RectCollisionEvent(
                        ent,
                        cr.rect,
                        collision_rects[current_index+1+i][0],
                        collision_rects[current_index+1+i][1].rect
                    )
                )
            current_index += 1

