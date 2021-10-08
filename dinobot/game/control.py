from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PIL import ImageGrab

import pyautogui
import time
import numpy as np

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
        self.relativeCanvasPos = (self.canvasPos['x']*1.55, self.canvasPos['y']*3.3, (self.canvasPos['x']*1.55)+(self.canvasSize['width']*1.5), (3.3*self.canvasPos['y'])+self.canvasSize['height']*1.75)
    

    def close_game(self):
        print("Closing game...")
        self.driver.close()

    def start_game(self):
        print("Starting game...")
        self.actionChains.move_to_element(self.dinoCanvas)
        self.actionChains.click()
        self.actionChains.send_keys(Keys.SPACE)
        self.actionChains.perform()

    def act_obstacle(self):
        canvasImg = ImageGrab.grab(self.relativeCanvasPos).convert('L')
        obstacle = canvasImg.crop((canvasImg.size[0]*0.35, canvasImg.size[1]*0.5, canvasImg.size[0]*0.45, canvasImg.size[1]*0.7))
        if(np.sum(np.array(obstacle)) < self.all_white(obstacle)):
            self.actionChains.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        return(self.game_over(canvasImg))

    def game_over(self, canvas):
        im = canvas.crop((canvas.size[0]*0.7, 0, canvas.size[0]*0.77, canvas.size[1]*0.11))
        pixels = np.array(im)
        return(np.sum(pixels) < 450000)


    def all_white(self, obstacleFrame):
        return(obstacleFrame.size[0]*obstacleFrame.size[1]*247)