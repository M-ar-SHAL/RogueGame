class Player:
    def __init__(self, game_map):
        self.y, self.x = game_map.place_entity()
        self.hp = 10
        self.score = 0

    def move(self, dy, dx, game_map):
        ny, nx = self.y + dy, self.x + dx
        if game_map.is_walkable(ny, nx):
            self.y, self.x = ny, nx
