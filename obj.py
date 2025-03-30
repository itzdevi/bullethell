from graphics import Graphics


class Obj:
    def __init__(self):
        self.x: int = 0
        self.y: int = 0

    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def get_position(self):
        return self.x, self.y
    
    def update(self, dt: float): ...
    def draw(self, graphics: Graphics): ...