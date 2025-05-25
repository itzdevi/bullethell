import math
import pygame

from constants import RESOLUTION
from agent import Action
from obj import Obj

MOVE_SPEED = 400
SIZE = 30, 30
COLOR = 0, 0, 255

class Player(Obj):
    def __init__(self):
        super().__init__()
        self.set_position((0, 0))
        self.set_size(SIZE)
        self.set_color(COLOR)
        self.velocity = [0, 0]

    def update(self, dt):
        sq = self.velocity[0]**2 + self.velocity[1]**2
        if sq > 0:
            mag = math.sqrt(sq)
            self.x += self.velocity[0] / mag * MOVE_SPEED * dt
            self.y += self.velocity[1] / mag * MOVE_SPEED * dt

        max_x = RESOLUTION[0] / 2 - SIZE[0] / 2
        max_y = RESOLUTION[1] / 2 - SIZE[1] / 2
        self.x = max(-max_x, min(max_x, self.x))
        self.y = max(-max_y, min(max_y, self.y))

    def move(self, action: Action):
            self.velocity[0] = action.x
            self.velocity[1] = action.y

