from engine.esper.esper import Processor
from engine.systems.rect.tools import get_rect
from engine.systems.rectsprite.components import RectSpriteComponent


class RectSpriteProcessor(Processor):

    def __init__(self):
        pass

    def process(self, *args, **kwargs):

        for ent, rect_sprite in self.world.get_component(RectSpriteComponent):
            rect = get_rect(self.world, ent)
            if rect is None:
                continue

            rect_sprite.set_rect(rect)


