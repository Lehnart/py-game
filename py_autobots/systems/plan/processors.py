import pygame

from engine.esper import Processor
from engine.systems.sprite.components import SpriteComponent
from py_autobots.config import WORKSHOP_SPRITE
from py_autobots.systems.plan.components import PlanComponent
from py_autobots.systems.plan.events import CreatePlanEvent
from py_autobots.systems.ressource.components import Ressource


class PlanProcessor(Processor):

    def __init__(self):
        super().__init__()

    def process(self):
        for event in self.world.receive(CreatePlanEvent):

            if event.plan_name != "Workshop":
                continue

            sprite = WORKSHOP_SPRITE.copy()
            sprite.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
            plan = self.world.create_entity(
                PlanComponent({Ressource.WOOD: 1}),
                SpriteComponent(event.x, event.y, sprite, 1)
            )
