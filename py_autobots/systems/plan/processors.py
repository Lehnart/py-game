import pygame

from engine.esper import Processor
from engine.systems.rect.components import RectComponent
from engine.systems.sprite.components import SpriteComponent
from py_autobots.config import WORKSHOP_SPRITE, TILE_SIZE
from py_autobots.systems.holder.events import RemoveEvent
from py_autobots.systems.plan.components import PlanComponent
from py_autobots.systems.plan.events import CreatePlanEvent, AddRessourceEvent, BuildEvent
from py_autobots.systems.ressource.components import Ressource, RessourceComponent


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
                PlanComponent({Ressource.BRANCH: 1}),
                SpriteComponent(event.x, event.y, sprite, 1),
                RectComponent(event.x, event.y, TILE_SIZE, TILE_SIZE)
            )
            print("plan " + str(plan))

        for event in self.world.receive(AddRessourceEvent):

            event: AddRessourceEvent
            res_ent = event.res_ent
            dest_plan_ent = event.dest_plan_ent
            holder_ent = event.holder_ent

            if not self.world.entity_exists(dest_plan_ent):
                continue

            if not self.world.entity_exists(res_ent):
                continue

            if not self.world.has_component(res_ent, RessourceComponent):
                continue

            if not self.world.has_component(dest_plan_ent, PlanComponent):
                continue

            res_comp: RessourceComponent = self.world.component_for_entity(res_ent, RessourceComponent)
            plan_comp: PlanComponent = self.world.component_for_entity(dest_plan_ent, PlanComponent)

            if res_comp.res not in plan_comp.required_ressources:
                continue

            if plan_comp.required_ressources[res_comp.res] == plan_comp.current_ressources[res_comp.res]:
                continue

            plan_comp.current_ressources[res_comp.res] += 1
            print(res_comp.res)
            print(plan_comp.current_ressources[res_comp.res])

            self.world.delete_entity(res_ent, True)
            self.world.publish(RemoveEvent(holder_ent))

        for event in self.world.receive(BuildEvent):

            event: BuildEvent
            dest_plan_ent = event.dest_plan_ent

            if not self.world.entity_exists(dest_plan_ent):
                continue
            if not self.world.has_component(dest_plan_ent, PlanComponent):
                continue

            plan_comp: PlanComponent = self.world.component_for_entity(dest_plan_ent, PlanComponent)

            if plan_comp.required_ressources != plan_comp.current_ressources:
                continue

            self.world.remove_component(dest_plan_ent, PlanComponent)
            sprite_comp = self.world.component_for_entity(dest_plan_ent, SpriteComponent)
            sprite_comp.sprite = WORKSHOP_SPRITE.copy()
