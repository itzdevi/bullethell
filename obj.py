from graphics import Graphics

import pygame

class Obj:
    def __init__(self):
        self.x: int = 0
        self.y: int = 0
        self.width: int = 0
        self.height: int = 0
        self.color: tuple[int, int, int, int] = 0, 0, 0, 1

    def set_position(self, position: tuple[int, int]):
        self.x, self.y = position
    
    def get_position(self):
        return self.x, self.y
    
    def set_size(self, size: tuple[int, int]):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height
    
    def set_color(self, color: tuple[int, int, int, int]):
        self.color = color

    def get_color(self):
        return self.color
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, graphics: Graphics):
        graphics.draw_rect(self.color, self.get_position(), self.get_size())
    
    def update(self, dt: float): ...