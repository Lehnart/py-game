from typing import Tuple

from engine.esper import Event


class OutOfLimitEvent(Event):

    def __init__(
            self,
            ent: int,
            r: Tuple[float, float, float, float],
            cr: [float, float, float, float],
            limits: Tuple[float, float, float, float]
    ):
        super().__init__()
        self.ent = ent
        self.r = r
        self.cr = cr
        self.limits = limits
