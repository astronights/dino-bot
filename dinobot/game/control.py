from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class GameControl():
    def __init__(self):
        self.DINO_URL="chrome://dino"
        self.driver = webdriver.Chrome()
        # self.actionChains = ActionChains(self.driver)

    def load_game(self):
        try:
            self.driver.get(self.DINO_URL)
        except Exception:
            pass

    def close_game(self):
        self.driver.close()

    # def start_game(self):
        # self.actionChains.send_keys(Keys.SPACE).perform()