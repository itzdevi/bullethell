from enemy import Enemy

from math import sin, cos, radians

class Bullet(Enemy):
    def __init__(self, position: tuple[float, float], size: float, speed: float, direction: float):
        super().__init__(False)
        self.set_size((size, size))
        self.set_position(position)
        self.speed = speed
        self.direction = direction

    def update(self, dt):
        super().update(dt)
        speed_x = self.speed * cos(radians(self.direction)) * dt
        speed_y = self.speed * sin(radians(self.direction)) * dt
        self.set_position((self.get_position()[0] + speed_x, self.get_position()[1] + speed_y))