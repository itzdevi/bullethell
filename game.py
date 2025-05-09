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
        self.spawner.spawn_horizontal(5)
        while should_run:
            dt = clock.tick(FRAMERATE) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    should_run = False
        
            self.player.update(dt)
            self.spawner.update(dt)

            self.graphics.clear()
            self.player.draw(self.graphics)
            self.spawner.draw(self.graphics)
            self.graphics.flip()