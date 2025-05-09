import math
import pygame

from constants import RESOLUTION
from obj import Obj

MOVE_SPEED = 300
SIZE = 50, 50
COLOR = 0, 0, 255

class Player(Obj):
    def __init__(self):
        super().__init__()
        self.set_position((0, 0))
        self.set_size(SIZE)
        self.set_color(COLOR)

    def update(self, dt):
        self.handle_move(dt)

    def handle_move(self, dt):
        keys = pygame.key.get_pressed()
        input_vec = [0, 0]
        if keys[pygame.K_w]:
            input_vec[1] = -1
        if keys[pygame.K_s]:
            input_vec[1] = 1
        if keys[pygame.K_a]:
            input_vec[0] = -1
        if keys[pygame.K_d]:
            input_vec[0] = 1

        sq = input_vec[0]**2 + input_vec[1]**2
        if sq > 0:
            mag = math.sqrt(sq)
            self.x += input_vec[0] / mag * MOVE_SPEED * dt
            self.y += input_vec[1] / mag * MOVE_SPEED * dt

        max_x = RESOLUTION[0] / 2 - SIZE[0] / 2
        max_y = RESOLUTION[1] / 2 - SIZE[1] / 2
        self.x = max(-max_x, min(max_x, self.x))
        self.y = max(-max_y, min(max_y, self.y))