import pygame
from agent import Agent
from enemies.rect import Rect
from graphics import Graphics
from player import Player

class Environment:
    def __init__(self, agent: Agent):
        self.agent = agent
        self.player = Player()
        self.enemies = [Rect((0, -100), (50, 50), 30)]

    def update(self, dt):
        action = self.agent.get_action()
        self.player.move(action)
        self.player.update(dt)

        for e in self.enemies: e.update(dt)
        self.apply_collisions()

    def draw(self, graphics: Graphics):
        for e in self.enemies: e.draw(graphics)
        self.player.draw(graphics)

    def apply_collisions(self):
        for enemy in self.enemies:
            if self.aabb(self.player.get_rect(), enemy.get_rect()):
                print("damage!")

    def aabb(self, rect1: pygame.Rect, rect2: pygame.Rect) -> bool:
        return rect1.colliderect(rect2)