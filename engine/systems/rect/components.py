class RectComponent:

    def __init__(self, x: float, y: float, w: float, h: float):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def move(self, dx: float, dy: float):
        self.x += dx
        self.y += dy


class RectSpeedComponent:

    def __init__(self, vx: float, vy: float):
        self.vx = vx
        self.vy = vy


class RectBounceComponent:
    pass


class RectLimitComponent:

    def __init__(self, x_min: float, x_max: float, y_min: float, y_max: float):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
