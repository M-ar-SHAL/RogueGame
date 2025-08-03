class Treasure:
    def __init__(self, game_map):
        self.y, self.x = game_map.place_entity()

    def relocate(self, game_map):
        self.y, self.x = game_map.place_entity()
