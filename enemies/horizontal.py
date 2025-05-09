from enemy import Enemy

from constants import RESOLUTION

class Horizontal(Enemy):
    def __init__(self):
        super().__init__()
        self.set_color(self.color)
        self.set_size((RESOLUTION[0], 30))
        self.set_position((0, 0))