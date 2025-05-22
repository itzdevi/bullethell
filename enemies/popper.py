from enemies.rect import Rect


class Popper(Rect):
    def __init__(self, position: tuple[float, float], max_size: float, time: float):
        super().__init__(position, (0, 0), time)
        self.max_size = max_size
        self.time = time

    def update(self, dt):
        super().update(dt)
        elapsed = self.time - self.timer
        progress = elapsed / self.time
        progress_rel = (progress % 0.5) * 2
        progress_rel_inv = 1 - progress_rel
        if progress < 0.5:
            self.set_size((progress_rel * self.max_size, progress_rel * self.max_size))
        else:
            self.set_size((progress_rel_inv * self.max_size, progress_rel_inv * self.max_size))




