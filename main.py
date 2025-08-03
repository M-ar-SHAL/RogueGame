from game.player import Player
from game.enemy import Enemy
from game.map import Map
from game.items import Treasure
from engine import GameEngine
import curses

def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    game_map = Map(40, 20)
    player = Player(game_map)
    enemy = Enemy(game_map)
    treasure = Treasure(game_map)
    engine = GameEngine(stdscr, game_map, player, enemy, treasure)

    engine.run()

if __name__ == "__main__":
    curses.wrapper(main)
