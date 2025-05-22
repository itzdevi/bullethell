from enemy import Enemy

class EnemySpawn:
    def __init__(self, enemy: Enemy, delay: float):
        self.enemy = enemy
        self.delay = delay

class Sequence:
    def __init__(self, spawns: list[EnemySpawn]):
        self.spawns = spawns
        self.timer = 0

    def start(self):
        self.timer = 0

    def get_active_enemies(self):
        return [x.enemy for x in self.spawns if x.delay <= self.timer and not x.enemy.should_destroy()]

    def update(self, dt):
        self.timer += dt