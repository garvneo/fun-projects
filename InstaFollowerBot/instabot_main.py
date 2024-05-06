from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import random

# Additional Imports
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Note: this is old code and created in rush for functionality implementattion
# and fun only, hence you see all code is in one file and didn't use env vars or db.
# Will be modifying all of this in free time.


CHROME_DRIVER_PATH = "D:\chromedriver.exe"
SIMILAR_ACCOUNT = "_anime_drawinsgs"
USERNAME = "dummy@123"
PASSWORD = "dummy"

chrome_driver_path = Service("D:\chromedriver.exe")


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(service=chrome_driver_path)

    def login(self):
        print("100")
        self.driver.get("https://www.instagram.com/accounts/login/")
        print("1025")
        time.sleep(10)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(15)
        followers = self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        )
        followers.click()
        print(5252)
        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]")
        print("m", modal)
        for i in range(5):
            time.sleep(random.randint(1000, 1600) / 1000)
            self.driver.implicitly_wait(10)
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", modal
            )
            print(i, "jai ho")
            # time.sleep(4)

    def follow(self):
        self.driver.implicitly_wait(10)
        time.sleep(10)

        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        button_subset = 5 if len(all_buttons) > 5 else len(all_buttons)
        for buttons in all_buttons[:button_subset]:
            if buttons.text == "Follow":
                self.driver.implicitly_wait(10)
                time.sleep(random.randint(1000, 1600) / 1000)
                buttons.click()
            elif buttons.text != "Follow":
                cancel_button = self.driver.find_elements(
                    By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[2]"
                )
                cancel_button.click()

            elif buttons.text == "Following":
                unfollow_buttons = self.driver.find_element(
                    By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[1]"
                )
                self.driver.implicitly_wait(10)
                time.sleep(random.randint(1000, 1600) / 1000)
                unfollow_buttons.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
