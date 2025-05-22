from enemies.rect import Rect

class Popper(Rect):
    def __init__(self, position: tuple[float, float], max_size: float, time: float):
        super().__init__(position, (0, 0), time)
        self.max_size = max_size
        self.time = time

    def update(self, dt):
        super().update(dt)
        # Calculate progress from 0 to 1
        progress = self.timer / self.time
        
        # Create smooth grow/shrink cycle
        if progress < 0.5:
            # Growing phase: 0 to 1
            scale = progress * 2
        else:
            # Shrinking phase: 1 to 0
            scale = 2 * (1 - progress)
        
        current_size = self.max_size * scale
        self.set_size((current_size, current_size))