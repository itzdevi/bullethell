from droplet import Droplet
from enemy import Enemy
import random


class RainGenerator(Enemy):
    def __init__(self, frequency):
        self.droplets: list[Droplet] = []
        self.frequency = frequency
        self.debounce = 0

    def update(self, dt):
        self.debounce += dt
        if self.debounce >= self.frequency:
            self.debounce = 0
            y = -450
            x = random.randint(-300, 300)
            self.droplets.append(Droplet((x, y)))
        for droplet in self.droplets:
            droplet.update(dt)
        self.droplets = [droplet for droplet in self.droplets if droplet.y < 450]

        print(len(self.droplets))

    def draw(self, graphics):
        for droplet in self.droplets:
            droplet.draw(graphics)