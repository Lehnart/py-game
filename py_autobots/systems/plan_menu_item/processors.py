import pygame

from engine.esper import Processor
from engine.systems.sprite_string.events import SetColorEvent
from py_autobots.systems.plan_menu_item.components import PlanMenuItemComponent
from py_autobots.systems.plan_menu_item.events import SelectPlanMenuItem, UnselectPlanMenuItem


class PlanMenuItemProcessor(Processor):

    def __init__(self):
        super().__init__()

    def process(self):
        for event in self.world.receive(SelectPlanMenuItem):
            if not self.world.entity_exists(event.ent):
                continue

            if not self.world.has_component(event.ent, PlanMenuItemComponent):
                continue

            c = self.world.component_for_entity(event.ent, PlanMenuItemComponent)
            c.is_selected = True

            self.world.publish(SetColorEvent(event.ent, pygame.Color(255, 0, 0)))

        for event in self.world.receive(UnselectPlanMenuItem):
            if not self.world.entity_exists(event.ent):
                continue

            if not self.world.has_component(event.ent, PlanMenuItemComponent):
                continue

            c = self.world.component_for_entity(event.ent, PlanMenuItemComponent)
            c.is_selected = False

            self.world.publish(SetColorEvent(event.ent, pygame.color.Color(255, 255, 255)))
