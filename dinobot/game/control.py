from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class GameControl():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("detach", True)
        options.add_argument("--start-maximized")
        self.DINO_URL="http://127.0.0.1:5000"
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        print(self.driver.window_handles)
        # self.driver.set_network_conditions(offline=True, latency=5, throughput=500 * 1024)
        self.actionChains = ActionChains(self.driver)

    def load_game(self):
        self.driver.get(self.DINO_URL)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_game(self):
        self.driver.close()

    def start_game(self):
        print("Starting game...")
        self.actionChains.click(self.driver.find_element_by_id("dino-frame")).send_keys(Keys.SPACE).perform()