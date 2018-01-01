class CoordonateAbsolute:
    def __init__(self, x0, y0, scale):
        self.x0 = x0
        self.y0 = y0
        self.scale = scale

    def x(self, relative_x):
        return self.x0 + relative_x * self.scale

    def y(self, relative_y):
        pass
