from time import sleep
from selenium import webdriver
import pytest
from testcases.uitest.pages.test_page import Page


class TestPage(object):

    @pytest.fixture()
    def fix_fun(self):
        self.driver = webdriver.Chrome()
        self.testPage = Page(self.driver)
        yield
        self.driver.quit()

    @pytest.mark.usefixtures('fix_fun')
    def test_01_bd(self):
        self.testPage.open()
        self.testPage.send_text('selenium')
        sleep(2)

        self.testPage.click_btn()
        sleep(5)

        source = self.driver.page_source
        assert 'selenium' in source


if __name__ == '__main__':
    pytest.main(["-sv", __file__])
