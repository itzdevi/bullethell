from enemies.rect import Rect
from enemies.popper import Popper
from enemies.chaser import Chaser
from player import Player
from sequence import EnemySpawn, Sequence
import random
import math
from typing import List
from random import choice

# A more aggressive wall of poppers that trap the player
popper_wall = Sequence([
    # Left side
    EnemySpawn(Popper((-300, -200), 120, 2.0), 0),
    EnemySpawn(Popper((-300, 0), 120, 2.0), 0.2),
    EnemySpawn(Popper((-300, 200), 120, 2.0), 0.4),
    # Right side
    EnemySpawn(Popper((300, -200), 120, 2.0), 0),
    EnemySpawn(Popper((300, 0), 120, 2.0), 0.2),
    EnemySpawn(Popper((300, 200), 120, 2.0), 0.4),
    # Additional middle poppers for extra pressure
    EnemySpawn(Popper((0, -300), 100, 1.5), 0.6),
    EnemySpawn(Popper((0, 300), 100, 1.5), 0.6),
])

def create_spiral_sequence(turns=3, rect_count=24):  # More turns, more rectangles
    spawns = []
    radius = 250  # Larger radius
    angle_step = 360 * turns / rect_count
    delay_step = 0.1  # Faster spawn rate
    
    for i in range(rect_count):
        angle = i * angle_step
        rad_angle = angle * 3.14159 / 180
        x = radius * math.cos(rad_angle)
        y = radius * math.sin(rad_angle)
        spawns.append(
            EnemySpawn(Rect((x, y), (50, 50), 2.0), i * delay_step)
        )
    
    return Sequence(spawns)

def create_random_popper_field(count=25, duration=3.0):  # More poppers, shorter duration
    spawns = []
    for i in range(count):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        delay = random.uniform(0, 1.0)  # Faster spawn rate
        size = random.randint(60, 140)  # Larger poppers
        spawns.append(
            EnemySpawn(Popper((x, y), size, duration), delay)
        )
    return Sequence(spawns)

def create_chaser_storm(player: Player):
    return Sequence([
        # Initial wave - two fast chasers
        EnemySpawn(Chaser((-300, -300), 35, 4.0, 250, player), 0),
        EnemySpawn(Chaser((300, 300), 35, 4.0, 250, player), 0.2),
        # Second wave - three medium chasers
        EnemySpawn(Chaser((-400, 0), 30, 4.0, 300, player), 1.0),
        EnemySpawn(Chaser((400, 0), 30, 4.0, 300, player), 1.0),
        EnemySpawn(Chaser((0, -400), 30, 4.0, 300, player), 1.2),
        # Final wave - four very fast chasers
        EnemySpawn(Chaser((-300, -300), 25, 3.0, 350, player), 2.0),
        EnemySpawn(Chaser((300, -300), 25, 3.0, 350, player), 2.0),
        EnemySpawn(Chaser((-300, 300), 25, 3.0, 350, player), 2.0),
        EnemySpawn(Chaser((300, 300), 25, 3.0, 350, player), 2.0),
    ])

# Update the global instances
spiral_attack = create_spiral_sequence()
popper_field = create_random_popper_field()

# Add after existing sequences
def create_pinwheel_attack(player: Player) -> Sequence:
    """Creates a pinwheel of chasers that rotate around the screen"""
    spawns = []
    num_chasers = 8
    radius = 400
    
    for i in range(num_chasers):
        angle = i * (360 / num_chasers)
        rad_angle = angle * math.pi / 180
        x = radius * math.cos(rad_angle)
        y = radius * math.sin(rad_angle)
        spawns.append(
            EnemySpawn(Chaser((x, y), 30, 5.0, 300, player), i * 0.2)
        )
    return Sequence(spawns)

def create_box_trap() -> Sequence:
    """Creates a box of rectangles that shrinks around the player"""
    size = 50
    return Sequence([
        # Top row
        EnemySpawn(Rect((-400, -400), (size, size), 3.0), 0),  # Removed speed parameter
        EnemySpawn(Rect((-200, -400), (size, size), 3.0), 0.2),
        EnemySpawn(Rect((200, -400), (size, size), 3.0), 0.2),
        EnemySpawn(Rect((400, -400), (size, size), 3.0), 0),
        # Bottom row
        EnemySpawn(Rect((-400, 400), (size, size), 3.0), 0),
        EnemySpawn(Rect((-200, 400), (size, size), 3.0), 0.2),
        EnemySpawn(Rect((200, 400), (size, size), 3.0), 0.2),
        EnemySpawn(Rect((400, 400), (size, size), 3.0), 0),
    ])

def create_popper_snake(length: int = 8) -> Sequence:
    """Creates a snake-like pattern of poppers"""
    spawns = []
    spacing = 100
    
    for i in range(length):
        x = -400 + (i * spacing)
        y = math.sin(i * 0.5) * 200
        spawns.append(
            EnemySpawn(Popper((x, y), 80, 2.0), i * 0.3)
        )
    return Sequence(spawns)

# Update the random sequence selector to include new patterns
def get_random_sequence(player: Player) -> Sequence:
    """Returns a random attack sequence"""
    sequences: List[Sequence] = [
        popper_wall,
        create_spiral_sequence(),
        create_random_popper_field(),
        create_chaser_storm(player),
        create_pinwheel_attack(player),
        create_box_trap(),
        create_popper_snake()
    ]
    return choice(sequences)