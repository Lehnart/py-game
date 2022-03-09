import pygame

from engine.esper import World
from engine.systems.event.processors import EventProcessor
from engine.systems.input.components import InputComponent
from engine.systems.input.processors import InputProcessor
from engine.systems.limit_rect.components import RectLimitComponent
from engine.systems.limit_rect.processors import LimitRectProcessor
from engine.systems.rect.components import RectComponent
from engine.systems.rect.processors import RectProcessor
from engine.systems.render.components import WindowComponent
from engine.systems.render.processors import RenderProcessor
from engine.systems.speed.events import MoveEvent
from engine.systems.sprite.components import SpriteComponent
from engine.systems.sprite.processors import SpriteProcessor
from rogue_hold.config import WINDOW_SIZE, FRAME_RATE, PLAYER_SPRITE_PARAMETERS, PLAYER_X0, PLAYER_Y0, \
    GRASS_SPRITE_PARAMETERS
from rogue_hold.sprites import get_sprite


class RogueHold(World):

    def __init__(self):
        super().__init__()
        self._is_running: bool = True

        # Window entity
        window = WindowComponent(WINDOW_SIZE)
        self.create_entity(window)

        # Player Entity
        player_sprite = get_sprite(*PLAYER_SPRITE_PARAMETERS)
        player_sprite_component = SpriteComponent(PLAYER_X0, PLAYER_Y0, player_sprite, 2)
        player_rect = RectComponent(PLAYER_X0, PLAYER_Y0, player_sprite.get_size()[0], player_sprite.get_size()[1])
        player_rect_limit = RectLimitComponent(0, WINDOW_SIZE[0], 0, WINDOW_SIZE[1])
        player_entity = self.create_entity(player_sprite_component, player_rect, player_rect_limit)

        movement = player_sprite.get_size()[0]
        self.add_component(
            player_entity,
            InputComponent(
                {
                    pygame.K_UP: lambda w: w.publish(MoveEvent(player_entity, 0, -movement)),
                    pygame.K_DOWN: lambda w: w.publish(MoveEvent(player_entity, 0, +movement)),
                    pygame.K_LEFT: lambda w: w.publish(MoveEvent(player_entity, -movement, 0)),
                    pygame.K_RIGHT: lambda w: w.publish(MoveEvent(player_entity, +movement, 0)),
                },
                is_repeat=False
            )
        )

        # Ground
        grass_sprite = get_sprite(*GRASS_SPRITE_PARAMETERS)
        gw, gh = grass_sprite.get_size()
        for x0 in range(0, WINDOW_SIZE[0], gw):
            for y0 in range(0, WINDOW_SIZE[1], gh):
                grass_sprite_component = SpriteComponent(x0, y0, grass_sprite)
                grass_rect = RectComponent(x0, y0, gw, gh)
                self.create_entity(grass_sprite_component, grass_rect)


        self.add_processor(InputProcessor(), 20)
        self.add_processor(EventProcessor(), 11)
        self.add_processor(RenderProcessor(FRAME_RATE), 9)
        self.add_processor(SpriteProcessor(), 8)
        self.add_processor(RectProcessor(), 7)
        self.add_processor(LimitRectProcessor(), 6)

    def is_running(self) -> bool:
        return self._is_running


def run():
    game_world = RogueHold()
    while game_world.is_running():
        game_world.process()


if __name__ == '__main__':
    run()
