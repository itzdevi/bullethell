import pygame

from constants import *
from player import Player

class Graphics:
    def __init__(self, player: Player):
        self.surface = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption(TITLE)

        self.player = player

    def render(self):
        self.surface.fill(BACKGROUND_COLOR)
        self.render_player(self.player)

        pygame.display.flip()
    
    def render_player(self, player: Player):
        pos = self.world_to_screen_pos(player.get_position(), PLAYER_SIZE)
        rect = pygame.Rect(*pos, *PLAYER_SIZE)
        pygame.draw.rect(self.surface, PLAYER_COLOR, rect)

    def world_to_screen_pos(self, position, size):
        return position[0] + RESOLUTION[0] / 2 - size[0] / 2, position[1] + RESOLUTION[1] / 2 - size[0] / 2