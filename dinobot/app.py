import time
from game.control import GameControl

def run():
    game = GameControl()
    game.load_game()
    game.start_game()
    while not game.act_obstacle():
        continue
    game.close_game()