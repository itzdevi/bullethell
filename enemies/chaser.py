from enemies.rect import Rect
from player import Player

import math

class Chaser(Rect):
    def __init__(self, start_position: tuple[float, float], size: float, time: float, speed: float, player: Player):
        super().__init__(start_position, (size, size), time)
        self.player = player
        self.speed = speed

    def update(self, dt):
        super().update(dt)
        x, y = self.get_position()
        dir_vec = [0, 0]
        if x != self.player.x:
            dir_vec[0] = self.player.x - x
        if y != self.player.y:
            dir_vec[1] = self.player.y - y

        sq = dir_vec[0]**2 + dir_vec[1]**2
        if sq > 0:
            mag = math.sqrt(sq)
            self.x += dir_vec[0] / mag * self.speed * dt
            self.y += dir_vec[1] / mag * self.speed * dt