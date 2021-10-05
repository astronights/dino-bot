from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PIL import Image, ImageGrab
import pyautogui

class GameControl():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("detach", True)
        self.DINO_URL="http://127.0.0.1:5000"
        self.driver = webdriver.Chrome(options=options)
        self.actionChains = ActionChains(self.driver)

    def load_game(self):
        self.driver.get(self.DINO_URL)
        self.pos = self.driver.get_window_rect()
        self.driver.minimize_window()
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"dino-frame")))
        self.dinoCanvas = self.driver.find_elements_by_class_name("runner-canvas")[0]
        self.canvasPos = self.dinoCanvas.location
        self.canvasSize = self.dinoCanvas.size

    def close_game(self):
        print("Closing game...")
        self.driver.close()

    def start_game(self):
        print("Starting game...")
        self.actionChains.move_to_element(self.dinoCanvas)
        self.actionChains.click()
        self.actionChains.send_keys(Keys.SPACE)
        self.actionChains.perform()

    def map_items(self):
        print("Mapping score...")
        image = pyautogui.screenshot(region=(self.canvasPos['x'], self.canvasPos['y'], self.canvasPos['x'] + self.canvasSize['height'], self.canvasPos['y'] + self.canvasSize['width']))
        image.show()