from obj import Obj

COLOR = 255, 255, 255
WARNING_COLOR = 255, 0, 0

class Enemy(Obj):
    def __init__(self):
        super().__init__()
        self.color = COLOR
        self.warning_color = WARNING_COLOR