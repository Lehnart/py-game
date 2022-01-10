from engine.esper import Processor
from engine.systems.render.events import DrawSpriteEvent
from engine.systems.sprite.components import SpriteComponent


class SpriteProcessor(Processor):

    def __init__(self):
        super().__init__()

    def process(self):
        for _, sprite_comp in self.world.get_component(SpriteComponent):
            self.world.publish(DrawSpriteEvent(sprite_comp.sprite, (sprite_comp.x0, sprite_comp.y0)))
