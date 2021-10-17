from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
import unittest
import HtmlTestRunner
from banner import banner
from Pages.xss_page import Homepage
import yaml
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException

print(banner())

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome('/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def test_login_valid(self):
        driver = self.driver
        driver.get('http://demo.testfire.net')
        time.sleep(3)

        login = Homepage(driver)
        time.sleep(3)
        login.enter_payload("<script>alert(1)</script>"+ Keys.ENTER)
        time.sleep(5)
        try:
            obj = driver.switch_to.alert
            msg = obj.text
            print("Alert shows following msg:" + msg)
            with open('description.yml') as file:
                info = yaml.load(file)
                print(info)
        except UnexpectedAlertPresentException:
            pass
        except NoAlertPresentException:
            pass
        Alert(self.driver).accept()

        with open('description.yml') as file:
            info = yaml.load(file)
            print(info)
    
    def test_login_valid2(self):
        driver = self.driver
        driver.get('https://www.google.com/')
        time.sleep(3)

        google = Homepage(driver)
        time.sleep(3)
        google.enter_payload_google_textbox("<script>alert(1)</script>" + Keys.ENTER)
        time.sleep(5)
        try:
            obj = driver.switch_to.alert
            msg = obj.text
            print("Alert shows following msg:" + msg)
        except UnexpectedAlertPresentException:
            pass
        except NoAlertPresentException:
            print("Site is safe from XSS")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/reports'))