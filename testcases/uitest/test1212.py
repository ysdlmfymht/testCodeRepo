from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By


class Test:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def test_setup(self):
        self.driver.get('https://www.baidu.com')
        sleep(2)

        self.driver.maximize_window()
        sleep(2)

        self.driver.find_element(By.ID, 'kw').send_keys('se')
        sleep(2)

        self.driver.find_element(By.ID, 'su').click()
        sleep(2)

        self.driver.quit()


if __name__ == '__main__':
    # Test().setup()
    pytest.main(["-sv"])
