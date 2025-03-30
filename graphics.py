import pygame

from constants import *

BACKGROUND_COLOR = 0, 0, 0

class Graphics:
    def __init__(self):
        self.surface = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption(TITLE)

    def clear(self):
        self.surface.fill(BACKGROUND_COLOR)

    def flip(self):
        pygame.display.flip()

    def draw_rect(self, color, position, size):
        rect = pygame.Rect(*self.world_to_screen_pos(position, size), size[0], size[1])
        pygame.draw.rect(self.surface, color, rect)

    def world_to_screen_pos(self, position, size):
        return position[0] + RESOLUTION[0] / 2 - size[0] / 2, position[1] + RESOLUTION[1] / 2 - size[0] / 2
        