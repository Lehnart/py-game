class RectComponent:

    def __init__(self, x :float, y:float, w:float, h:float):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def move(self, dx: float, dy: float):
        self.x += dx
        self.y += dy
