from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class GameControl():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("detach", True)
        ## Maximizing window leads to actions not working
        self.DINO_URL="http://127.0.0.1:5000"
        self.driver = webdriver.Chrome(options=options)
        self.actionChains = ActionChains(self.driver)

    def load_game(self):
        self.driver.get(self.DINO_URL)
        print(self.driver.get_window_position())
        print(self.driver.get_window_rect())
        print(self.driver.get_window_size())
        # self.driver.set_window_size()
        # self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_game(self):
        print("Closing game...")
        self.driver.close()

    def start_game(self):
        print("Starting game...")
        self.actionChains.click(self.driver.find_element_by_id("dino-frame")).send_keys(Keys.SPACE).perform()