from enemies.horizontal import Horizontal
from obj import Obj
from enemies.rain_generator import RainGenerator
from enemies.vertical import Vertical


class Spawner(Obj):
    def __init__(self):
        self.set_color((0, 0, 0))
        self.set_size((0, 0))
        self.set_position((0, 0))
        self.enemies = []

    def spawn_rain(self, frequency: float, duration: float):
        self.enemies.append([RainGenerator(frequency), duration])

    def spawn_horizontal(self, duration: float):
        self.enemies.append([Horizontal(), duration])

    def spawn_vertical(self, duration: float):
        self.enemies.append([Vertical(), duration])

    def update(self, dt):
        for enemy in self.enemies:
            enemy[0].update(dt)
            enemy[1] -= dt
            if enemy[1] <= 0:
                self.enemies.remove(enemy)

    def draw(self, graphics):
        for enemy in self.enemies:
            enemy[0].draw(graphics)