import pygame
from constants import *
from graphics import Graphics
from player import Player


class Game:
    def __init__(self):
        self.player = Player()
        self.graphics = Graphics(self.player)

    def start(self):
        clock = pygame.time.Clock()
        should_run = True
        while should_run:
            dt = clock.tick(FRAMERATE) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    should_run = False
        
            self.player.update(dt)

            self.graphics.render()