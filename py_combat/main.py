import pygame

from engine.esper import World
from engine.systems.input.components import InputComponent
from engine.systems.input.processors import InputProcessor
from engine.systems.limit_rect.components import RectLimitComponent
from engine.systems.orientation.components import OrientationComponent
from engine.systems.orientation.events import RotateEvent
from engine.systems.orientation.processors import OrientationProcessor
from engine.systems.rect.components import RectComponent
from engine.systems.rect.processors import RectProcessor
from engine.systems.render.components import WindowComponent
from engine.systems.render.processors import RenderProcessor
from engine.systems.speed.events import MoveEvent
from engine.systems.sprite.components import SpriteComponent
from engine.systems.sprite.processors import SpriteProcessor
from py_combat.config import *


class PyCombat(World):

    def __init__(self):
        super().__init__()
        self._is_running: bool = True

        # Window entity
        window = WindowComponent(WINDOW_SIZE)
        self.create_entity(window)

        # left tank entity
        rect = RectComponent(*TANK_LEFT_RECT)
        rect_limit = RectLimitComponent(*WINDOW_LIMITS)
        sprite = SpriteComponent(TANK_LEFT_RECT[0], TANK_LEFT_RECT[1], TANK_SPRITE)
        orientation = OrientationComponent(0)
        tank_left = self.create_entity(rect, rect_limit, sprite, orientation)

        self.add_component(
            tank_left,
            InputComponent(
                {
                    pygame.K_UP: lambda w: w.publish(MoveEvent(tank_left, 0, -w.process_dt * TANK_SPEED)),
                    pygame.K_DOWN: lambda w: w.publish(MoveEvent(tank_left, 0, +w.process_dt * TANK_SPEED)),
                    pygame.K_LEFT: lambda w: w.publish(RotateEvent(tank_left, -w.process_dt * TANK_ROTATION_SPEED)),
                    pygame.K_RIGHT: lambda w: w.publish(RotateEvent(tank_left, +w.process_dt * TANK_ROTATION_SPEED)),
                }
            )
        )

        self.add_processor(InputProcessor(), 20)
        self.add_processor(RectProcessor(), 18)
        self.add_processor(OrientationProcessor(), 17)
        self.add_processor(SpriteProcessor(), 16)
        self.add_processor(RenderProcessor(), 9)

    def is_running(self) -> bool:
        return self._is_running


def run():
    game_world = PyCombat()
    while game_world.is_running():
        game_world.process()


if __name__ == '__main__':
    run()
