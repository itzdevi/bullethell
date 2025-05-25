import pygame

class Action:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Agent:
    def get_action(self) -> Action: ...

class KeyboardAgent(Agent):
    def get_action(self):
        keys = pygame.key.get_pressed()
        input_vec = [0, 0]
        if keys[pygame.K_w]:
            input_vec[1] = -1
        if keys[pygame.K_s]:
            input_vec[1] = 1
        if keys[pygame.K_a]:
            input_vec[0] = -1
        if keys[pygame.K_d]:
            input_vec[0] = 1
        return Action(*input_vec)