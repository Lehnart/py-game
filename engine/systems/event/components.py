from typing import Callable, Dict, Type

from engine import esper
from engine.esper import Event


class EventComponent:

    def __init__(self, event_callbacks: Dict[Type[Event], Callable[[int, Event, esper.World], None]]):
        self.event_callbacks = event_callbacks
