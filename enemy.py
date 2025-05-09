from obj import Obj

COLOR = 255, 255, 255
WARNING_COLOR = 246, 238, 7

class Enemy(Obj):
    def __init__(self, warning: bool):
        super().__init__()
        self.color = COLOR
        self.warning = warning
        self.timer = 0

    def is_warning(self): return self.warning
    def set_warning(self, warning: bool): self.warning = warning

    def update(self, dt):
        if self.is_warning():
            self.set_color(WARNING_COLOR)
        else:
            self.set_color(COLOR)