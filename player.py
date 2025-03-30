import math
import pygame

from constants import MOVE_SPEED

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

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


    def get_position(self):
        return self.x, self.y