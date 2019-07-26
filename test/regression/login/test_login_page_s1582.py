import unittest
import json

from lib.ui.login_page import LoginPage
from lib.ui.home_page import HomePage
from lib.utils import create_driver

class TestLogins1582(unittest.TestCase) :

    def setUp(self):
        self.driver= create_driver.get_driver_instance()
        self.login= LoginPage(self.driver)
        self.home= HomePage(self.driver)

    def tearDown(self):
        self.driver.close()


    def test_valid_login_tc12345(self):
        data= json.load(open('./test/regression/login/testcaseid.json'))
        #Goto Login Page
        self.login.wait_for_login_page_to_load()
        #enter username
        self.login.get_username_textbox().send_keys(data['TC123456']['username'])
        #enter password
        self.login.get_password_textbox().send_keys(data['TC123456']['password'])
        #click on login button
        self.login.get_login_button().click()
        #wait for the page to load
        self.home.wait_for_login_page_to_load()
        #get title of the page
        actual_title=self.home.title
        expected_title= data['TC123456']['title']
        assert actual_title==expected_title
         #click on logout
        self.home.get_logout_button().click()

