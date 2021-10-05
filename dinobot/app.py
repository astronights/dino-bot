import time
from game.control import GameControl

def run():
    game = GameControl()
    game.load_game()
    game.map_items()
    game.start_game()
    # time.sleep(2)
    # game.close_game()