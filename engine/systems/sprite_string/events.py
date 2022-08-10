import pygame

from engine.esper import Event


class SetStringEvent(Event):

    def __init__(self, ent: int, txt: str):
        super().__init__()
        self.ent = ent
        self.txt = txt


class SetColorEvent(Event):

    def __init__(self, ent: int, color: pygame.Color):
        super().__init__()
        self.ent = ent
        self.color = color
