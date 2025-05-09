from enemy import Enemy

DROP_SPEED = 1200

class Droplet(Enemy):
    def __init__(self, start_position: tuple[int, int]):
        super().__init__()
        self.set_position(start_position)
        self.set_size((3, 10))
        self.set_color(self.color)

    def update(self, dt):
        self.set_position((self.x, self.y + DROP_SPEED * dt))