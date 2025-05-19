import pygame
from constants import *
from graphics import Graphics
from player import Player
from spawner import Spawner


class Game:
    def __init__(self):
        self.graphics = Graphics()
        self.player = Player()
        self.spawner = Spawner()

    def start(self):
        clock = pygame.time.Clock()
        should_run = True
        self.spawner.spawn_vertical(0.4, 1)
        while should_run:
            dt = clock.tick(FRAMERATE) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    should_run = False
        
            self.player.update(dt)
            self.spawner.update(dt)
            self.apply_collisions()

            self.graphics.clear()
            self.player.draw(self.graphics)
            self.spawner.draw(self.graphics)
            self.graphics.flip()

    def apply_collisions(self):
        for enemy in self.spawner.get_lst():
            if self.aabb(self.player.get_rect(), enemy.get_rect()):
                if not enemy.is_warning():
                    print("damage!")

    def aabb(self, rect1: pygame.Rect, rect2: pygame.Rect) -> bool:
        return rect1.colliderect(rect2)