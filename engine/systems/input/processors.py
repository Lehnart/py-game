import sys

import pygame

from engine.esper import Processor
from engine.systems.input.components import InputComponent


class InputProcessor(Processor):

    def __init__(self):
        super().__init__()

    def process(self):

        input_components = self.world.get_component(InputComponent)

        keys = pygame.key.get_pressed()
        for ent, input_component in input_components:
            for key in input_component.input_dicts :
                if keys[key] :
                    input_component.input_dicts[key](self.world)


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

