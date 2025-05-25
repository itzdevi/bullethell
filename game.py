import pygame
from agent import Agent
from constants import *
from environment import Environment
from graphics import Graphics
from player import Player
import sequences

class Game:
    def __init__(self, agent: Agent):
        self.graphics = Graphics()
        self.environment = Environment(agent)

    def start(self):
        clock = pygame.time.Clock()
        should_run = True
        while should_run:
            dt = clock.tick(FRAMERATE) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    should_run = False

            self.environment.update(dt)

            # self.apply_collisions()

            self.graphics.clear()
            self.environment.draw(self.graphics)
            self.graphics.flip()
    
    def change_sequence(self, new_sequence):
        self.sequence = new_sequence
        self.sequence.start()
        self.enemies.clear()