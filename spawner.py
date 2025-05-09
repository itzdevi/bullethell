from obj import Obj
from enemies.horizontal import Horizontal
from enemies.vertical import Vertical


class Spawner(Obj):
    def __init__(self):
        self.set_color((0, 0, 0))
        self.set_size((0, 0))
        self.set_position((0, 0))
        self.enemies = []

    def spawn_horizontal(self, warning_duration: float, duration: float):
        self.enemies.append([Horizontal(True), warning_duration, duration])

    def spawn_vertical(self, warning_duration: float, duration: float):
        self.enemies.append([Vertical(True), warning_duration, duration])

    def update(self, dt):
        for enemy in self.enemies:
            enemy[0].update(dt)
            if enemy[0].is_warning() and enemy[1] > 0:
                enemy[1] -= dt
                if enemy[1] <= 0:
                    enemy[0].set_warning(False)
            else:
                enemy[2] -= dt
            if enemy[2] <= 0:
                self.enemies.remove(enemy)

    def draw(self, graphics):
        for enemy in self.enemies:
            enemy[0].draw(graphics)