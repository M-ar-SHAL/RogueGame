import time
import curses
from game.map import WALL, FLOOR

DIRECTIONS = {
    'w': (-1, 0),
    's': (1, 0),
    'a': (0, -1),
    'd': (0, 1)
}

class GameEngine:
    def __init__(self, screen, game_map, player, enemy, treasure):
        self.screen = screen
        self.map = game_map
        self.player = player
        self.enemy = enemy
        self.treasure = treasure

    def draw(self):
        self.screen.clear()
        for y in range(self.map.height):
            for x in range(self.map.width):
                char = self.map.grid[y][x]
                if (y, x) == (self.player.y, self.player.x):
                    self.screen.addstr(y, x, '@', curses.color_pair(2))
                elif (y, x) == (self.enemy.y, self.enemy.x):
                    self.screen.addstr(y, x, 'E', curses.color_pair(3))
                elif (y, x) == (self.treasure.y, self.treasure.x):
                    self.screen.addstr(y, x, '$')
                else:
                    self.screen.addstr(y, x, char)
        self.screen.addstr(self.map.height, 0, f"HP: {self.player.hp}   Score: {self.player.score}", curses.color_pair(1))
        self.screen.refresh()

    def run(self):
        while self.player.hp > 0:
            self.draw()
            key = self.screen.getch()
            if chr(key) in DIRECTIONS:
                dy, dx = DIRECTIONS[chr(key)]
                self.player.move(dy, dx, self.map)

            self.enemy.update(self.map, self.player)

            if (self.player.y, self.player.x) == (self.enemy.y, self.enemy.x):
                self.player.hp -= 1

            if (self.player.y, self.player.x) == (self.treasure.y, self.treasure.x):
                self.player.score += 10
                self.treasure.relocate(self.map)

            time.sleep(0.1)

        self.screen.clear()
        self.screen.addstr(self.map.height // 2, self.map.width // 2 - 5, "GAME OVER", curses.color_pair(3))
        self.screen.refresh()
        time.sleep(2)
