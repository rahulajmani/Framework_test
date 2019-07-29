import unittest
from lib.ui.login_page import LoginPage
from lib.utils import create_driver
from selenium.webdriver.common.keys import Keys


class TestComponents(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver.get_driver_instance()
        self.login = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_framework_components(self):

        self.login.wait_for_login_page_to_load()
        self.login.get_username_textbox().send_keys('admin')
        self.login.get_password_textbox().send_keys('pass')
        self.login.get_login_button().click()
        actual_title = self.driver.title
        expected_title = 'actiTIME - Login'

        assert actual_title == expected_title,'passed'







