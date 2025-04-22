from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class TestPage(object):

    def test_01_bd(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        sleep(2)
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        sleep(2)
        self.driver.find_element(By.ID, 'su').click()
        sleep(5)

        source = self.driver.page_source
        assert 'selenium' in source
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(["-sv", __file__])
