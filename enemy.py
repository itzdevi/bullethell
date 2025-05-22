from obj import Obj

class Enemy(Obj):
    def __init__(self):
        super().__init__()

    def should_destroy(self) -> bool: ...
