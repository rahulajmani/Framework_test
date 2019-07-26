from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:

    def __int__(self,driver):
        self.driver=driver

    def wait_for_login_page_to_load(self):
        wait= WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_logout_button))

    def get_logout_button(self):
        try:
            return self.driver.find_element_by_id('logoutLink')
        except:
            return None






