from typing import Tuple

from engine.esper import Event


class SetRectSpritePosEvent(Event):

    def __init__(self, ent: int, pos: Tuple[int, int]):
        super().__init__()
        self.ent = ent
        self.pos = pos
