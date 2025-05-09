import pygame
from constants import *
from enemy import Enemy
from graphics import Graphics
from player import Player
from rain_generator import RainGenerator


class Game:
    def __init__(self):
        self.graphics = Graphics()
        self.player = Player()
        self.enemies: list[Enemy] = []

        self.enemies.append(RainGenerator(0.03))

    def start(self):
        clock = pygame.time.Clock()
        should_run = True
        while should_run:
            dt = clock.tick(FRAMERATE) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    should_run = False
        
            self.player.update(dt)

            for enemy in self.enemies:
                enemy.update(dt)

            self.graphics.clear()

            self.player.draw(self.graphics)
            for enemy in self.enemies:
                enemy.draw(self.graphics)
            
            self.graphics.flip()