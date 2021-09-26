from selenium import webdriver


class GameLoader():
    def __init__(self):
        self.DINO_URL="chrome://dino"
        self.driver = webdriver.Chrome()

    def load_game(self):
        self.driver.get(self.DINO_URL)

    def close_game(self):
        self.driver.close()