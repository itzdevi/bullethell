import pygame
from constants import *
from graphics import Graphics
from player import Player
import sequences

class Game:
    def __init__(self):
        self.graphics = Graphics()
        self.player = Player()
        self.enemies = []

    def start(self):
        clock = pygame.time.Clock()
        should_run = True
        seq_end = False
        seq_db = 0
        self.change_sequence(sequences.get_random_sequence(self.player))
        self.sequence.start()
        while should_run:
            dt = clock.tick(FRAMERATE) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    should_run = False

            self.player.update(dt)
            self.enemies = self.sequence.get_active_enemies()
            for e in self.enemies: e.update(dt)

            if len(self.enemies) == 0 and not seq_end:
                seq_end = True
                seq_db = 2
            if seq_end:
                if seq_db > 0:
                    seq_db -= dt
                else:
                    self.change_sequence(sequences.get_random_sequence(self.player))
                    seq_end = False

            self.apply_collisions()

            self.sequence.update(dt)

            self.graphics.clear()
            self.player.draw(self.graphics)
            for e in self.enemies: e.draw(self.graphics)
            self.graphics.flip()

    def apply_collisions(self):
        for enemy in self.enemies:
            if self.aabb(self.player.get_rect(), enemy.get_rect()):
                print("damage!")

    def aabb(self, rect1: pygame.Rect, rect2: pygame.Rect) -> bool:
        return rect1.colliderect(rect2)
    
    def change_sequence(self, new_sequence):
        self.sequence = new_sequence
        self.sequence.start()
        self.enemies.clear()