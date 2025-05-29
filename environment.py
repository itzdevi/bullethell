import pygame
from agent import Agent
from enemies.rect import Rect
from graphics import Graphics
from player import Player
import sequences

class Environment:
    def __init__(self, agent: Agent):
        self.agent = agent
        self.player = Player()
        self.enemies = []
        self.sequence = sequences.get_random_sequence(self.player)
        self.enemy_timer = 2
        self.enemy_end = True

    def update(self, dt):
        action = self.agent.get_action()
        self.player.move(action)
        self.player.update(dt)

        self.sequence.update(dt)
        self.enemies = self.sequence.get_active_enemies()

        if len(self.enemies) == 0:
            if not self.enemy_end:
                self.enemy_end = True
                self.enemy_debounce = 2
            else:
                if self.enemy_timer > 0:
                    self.enemy_timer -= dt
                else:
                    self.enemy_end = False
                    self.sequence = sequences.get_random_sequence(self.player)

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
    