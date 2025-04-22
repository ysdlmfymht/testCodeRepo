from selenium.webdriver.common.by import By

from testcases.uitest.pages.basePage import BasePage


class Page(BasePage):
    search_input = (By.ID, u'kw')
    search_btn = (By.ID, u'su')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def open(self):
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()

    def send_text(self, text):
        self.input_text(text, *self.search_input)

    def click_btn(self):
        self.click(*self.search_btn)
