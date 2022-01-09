from engine.esper import Processor
from engine.systems.collision_rect.components import CollisionRectComponent
from engine.systems.collision_rect.events import RectCollisionEvent


class CollisionRectProcessor(Processor):

    def __init__(self):
        pass

    def process(self, *args, **kwargs):

        collision_rects = self.world.get_component(CollisionRectComponent)
        rects = [cr.rect for _, cr in collision_rects]

        for ent, cr in collision_rects:
            collisions = cr.rect.collidelistall(rects)
            for i in collisions:
                self.world.publish(RectCollisionEvent(ent, cr, collision_rects[i][0], collision_rects[i][2]))
