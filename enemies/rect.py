from enemy import Enemy

class Rect(Enemy):
    def __init__(self, position: tuple[float, float], size: tuple[float, float], time: float):
        super().__init__()
        self.set_color((255, 255, 255, 1))
        self.set_position(position)
        self.set_size(size)
        self.timer = time

    def should_destroy(self):
        return self.timer <= 0

    def update(self, dt):
        self.timer -= dt