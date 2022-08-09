import sys

import pygame

from engine.esper import Processor
from engine.systems.input.components import InputComponent


class InputProcessor(Processor):

    def __init__(self):
        super().__init__()
        self.previously_pressed = {}

    def process(self):

        input_components = self.world.get_component(InputComponent)

        keys = pygame.key.get_pressed()
        for ent, input_component in input_components:
            for key in input_component.input_dicts:
                if input_component.is_repeat and keys[key]:
                    input_component.input_dicts[key](self.world, ent)
                elif not input_component.is_repeat and keys[key] and not self.previously_pressed[key]:
                    input_component.input_dicts[key](self.world, ent)

        self.previously_pressed = keys

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
