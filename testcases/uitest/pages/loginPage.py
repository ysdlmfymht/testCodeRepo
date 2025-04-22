from selenium.webdriver.common.by import By
from time import sleep

from testcases.uitest.pages.basePage import BasePage


class LoginPage(BasePage):
    search_input = (By.ID, 'kw')
    search_btn = (By.ID, 'su')

    def __init__(self, driver):
        super().__init__(driver)

    def open_bd(self):
        self.driver.get("https://www.baidu.com")

    def send_text(self):
        self.driver.find_element('selenium', *self.search_input)

    def click_btn(self):
        self.driver.find_element(*self.search_btn)
        sleep(3)
