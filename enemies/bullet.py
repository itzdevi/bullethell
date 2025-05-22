from constants import RESOLUTION
from enemies.rect import Rect
from enemy import Enemy

from math import sin, cos, radians

class Bullet(Rect):
    def __init__(self, position: tuple[float, float], size: float, speed: float, direction: float):
        super().__init__(position, (size, size), 0)
        self.speed = speed
        self.direction = direction
        self.size = size

    def should_destroy(self):
        return abs(self.x) > RESOLUTION[0] + self.size or abs(self.y) > RESOLUTION[0] + self.size

    def update(self, dt):
        super().update(dt)
        speed_x = self.speed * cos(radians(self.direction)) * dt
        speed_y = self.speed * sin(radians(self.direction)) * dt
        self.set_position((self.get_position()[0] + speed_x, self.get_position()[1] + speed_y))