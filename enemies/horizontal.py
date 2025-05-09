from enemy import Enemy

from constants import RESOLUTION

class Horizontal(Enemy):
    def __init__(self, warning: bool):
        super().__init__(warning)
        self.set_size((RESOLUTION[0], 30))
        self.set_position((0, 0))