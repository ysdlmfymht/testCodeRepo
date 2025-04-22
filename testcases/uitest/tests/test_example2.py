from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class TestPage(object):

    # @pytest.fixture()
    def __init__(self):
        self.driver = webdriver.Chrome()
        # yield self.driver
        # self.driver.quit()

    # @pytest.mark.dependency(depends=['testLogin'], scope='module')
    def test_bd_01(self):
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
