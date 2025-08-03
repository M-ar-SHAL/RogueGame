from utils.pathfinding import bfs

class Enemy:
    def __init__(self, game_map):
        self.y, self.x = game_map.place_entity()

    def update(self, game_map, player):
        path = bfs(game_map.grid, (self.y, self.x), (player.y, player.x))
        if path:
            self.y, self.x = path[0]
