from engine.esper import Processor
from py_autobots.systems.plan_menu.components import PlanMenuComponent
from py_autobots.systems.plan_menu.events import NextPlanEvent, PreviousPlanEvent
from py_autobots.systems.plan_menu_item.events import SelectPlanMenuItem, UnselectPlanMenuItem


class PlanMenuProcessor(Processor):

    def __init__(self):
        super().__init__()

    def process(self):
        for event in self.world.receive(NextPlanEvent):
            if not self.world.entity_exists(event.ent):
                continue

            if not self.world.has_component(event.ent, PlanMenuComponent):
                continue

            comp: PlanMenuComponent = self.world.component_for_entity(event.ent, PlanMenuComponent)
            self.world.publish(UnselectPlanMenuItem(comp.plans[comp.selected_index]))

            comp.selected_index += 1
            if comp.selected_index >= len(comp.plans):
                comp.selected_index = 0

            self.world.publish(SelectPlanMenuItem(comp.plans[comp.selected_index]))

        for event in self.world.receive(PreviousPlanEvent):
            if not self.world.entity_exists(event.ent):
                continue

            if not self.world.has_component(event.ent, PlanMenuComponent):
                continue

            comp: PlanMenuComponent = self.world.component_for_entity(event.ent, PlanMenuComponent)
            self.world.publish(UnselectPlanMenuItem(comp.plans[comp.selected_index]))

            comp.selected_index -= 1
            if comp.selected_index < 0:
                comp.selected_index = len(comp.plans) - 1
            self.world.publish(SelectPlanMenuItem(comp.plans[comp.selected_index]))
