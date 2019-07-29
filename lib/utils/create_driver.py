import pytest
from selenium.webdriver import Chrome,Firefox

def get_driver_instance():

    browser_type = pytest.config.option.browser.lower()
    os_name = pytest.config.option.system.lower()
    url_info=pytest.config.option.url.lower()


    if os_name == 'windows':
        if browser_type =='chrome':
            driver= Chrome('./Browser_server/chromedriver.exe')
        elif browser_type == 'firefox':
            driver=Firefox('./Browser_server/geckodriver.exe')

        driver.maximize_window()
        driver.implicitly_wait(30)

        if url_info=='test':
            driver.get('https://demo.actitime.com')
        elif url_info=='prod':
            driver.get('https://www.facebook.com')

        return driver




