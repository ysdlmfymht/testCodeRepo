from selenium import webdriver
from time import sleep


class Test:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def setup(self):
        self.driver.get('https://www.baidu.com')
        sleep(2)

        self.driver.maximize_window()
        sleep(2)

        # self.driver.quit()


if __name__ == '__main__':
    Test().setup()
