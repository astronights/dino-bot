import time
from game.control import GameControl

def run():
    game = GameControl()
    game.load_game()
    time.sleep(5)
    game.start_game()
    # time.sleep(2)
    # game.close_game()