from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import pyautogui

class GameControl():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("detach", True)
        ## Maximizing window leads to actions not working
        self.DINO_URL="http://127.0.0.1:5000"
        self.driver = webdriver.Chrome(options=options)
        self.actionChains = ActionChains(self.driver)
        self.screen = pyautogui.size()
        self.pos = None

    def load_game(self):
        self.driver.get(self.DINO_URL)
        self.pos = self.driver.get_window_rect()
        self.driver.minimize_window()
        self.driver.maximize_window()

    def close_game(self):
        print("Closing game...")
        self.driver.close()

    def start_game(self):
        print("Starting game...")
        frameElem = self.driver.find_element_by_id("dino-frame")
        self.actionChains.move_to_element_with_offset(frameElem, 10, 10)
        self.actionChains.click()
        self.actionChains.send_keys(Keys.SPACE)
        self.actionChains.perform()