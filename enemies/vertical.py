from enemy import Enemy

from constants import RESOLUTION

class Vertical(Enemy):
    def __init__(self):
        super().__init__()
        self.set_color(self.color)
        self.set_size((30, RESOLUTION[1]))
        self.set_position((0, 0))