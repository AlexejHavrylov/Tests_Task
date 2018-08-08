import unittest
# import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://intu.co.uk/shop/category/women")
        login_button = self.driver.find_element_by_class_name('js-login__label')
        login_button.click()
        driver = self.driver
        MyFrame = driver.find_element_by_tag_name("iframe")
        driver.switch_to.frame(MyFrame)

    def fill_in_form(self):
        driver = self.driver
        first_name_input = driver.find_element_by_id('textbox-1')

        last_name_input = driver.find_element_by_id('textbox-2')
        email_input = driver.find_element_by_id('textbox-3')
        birthday = driver.find_element_by_id('5_3')
        month = driver.find_element_by_id('5_2')
        year = driver.find_element_by_id('5_1')
        first_name_input.send_keys("John")
        last_name_input.send_keys('Smith')

        email_input.send_keys('j.smith@yahoo.com')
        birthday.send_keys(1)
        month.send_keys(1)
        year.send_keys(1970)
        driver.switch_to.default_content()
        driver.execute_script("window.scrollTo(0, 250)")

        MyFrame = driver.find_element_by_tag_name("iframe")
        driver.switch_to.frame(MyFrame)

    def test_01_sign_up(self):
        driver = self.driver

        self.fill_in_form()
        submit_button = driver.find_element_by_name("dsComplete")

        submit_button.click()
        url_str = driver.current_url

        expected_result = 'https://em.intu.co.uk/p/4LV8-2SF/confirmation'
        assert url_str == expected_result

    def test_02_sign_up_without_first_name(self):
        driver = self.driver
        self.fill_in_form()

        submit_button = driver.find_element_by_name("dsComplete")

        submit_button.click()

        error_string = driver.find_element_by_class_name('errortext').text

        expected_result = 'Please enter your first name'

        assert error_string == expected_result

    def test_03_check_h2_tag(self):
        driver = self.driver
        driver.switch_to.default_content()
        message = driver.find_element_by_tag_name('h2').text


        expected_result = 'Sign up to our emails'

        assert message == expected_result

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
