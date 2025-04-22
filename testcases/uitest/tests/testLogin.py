from selenium import webdriver

import pytest

from testcases.uitest.pages.loginPage import LoginPage


class TestLogin(object):
    login_data = []

    @pytest.fixture()
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.loginPage = LoginPage(self.driver)
        # yield self.driver
        # self.driver.quit()

    @pytest.mark.parametrize('username', 'passwd', login_data)
    def test_login(self, username, passwd):
        self.loginPage.find_element()
