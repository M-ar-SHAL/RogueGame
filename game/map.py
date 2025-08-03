import random

WALL = '#'
FLOOR = '.'

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[WALL for _ in range(width)] for _ in range(height)]
        self.generate()

    def generate(self):
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                self.grid[y][x] = FLOOR if random.random() > 0.2 else WALL

    def place_entity(self):
        while True:
            y = random.randint(1, self.height - 2)
            x = random.randint(1, self.width - 2)
            if self.grid[y][x] == FLOOR:
                return y, x

    def is_walkable(self, y, x):
        return 0 <= y < self.height and 0 <= x < self.width and self.grid[y][x] == FLOOR
