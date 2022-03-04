from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
import unittest
import HtmlTestRunner
from banner import banner
from Pages.page_repository import Homepage
import yaml
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException

print(banner())

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome('/Users/pravinshinde/Documents/Project/Automated_Project/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def test1_xss(self):
        driver = self.driver
        driver.get('http://demo.testfire.net')    # This website is vulnerable for XSS so below payload will alert
        time.sleep(8)

        login = Homepage(driver)
        time.sleep(5)
        login.enter_payload("<script>alert(1)</script>"+ Keys.ENTER)
        time.sleep(5)
        try:
            obj = driver.switch_to.alert
            msg = obj.text
            print("Alert shows following msg:" + msg)
            with open('description_for_xss.yml') as file:
                info = yaml.load(file)
                print(info)
        except UnexpectedAlertPresentException:
            print("Excetional Alert is present")
        except NoAlertPresentException:
            print("Site is safe from XSS")
        Alert(self.driver).accept()

    def test2_xss(self):
        driver = self.driver
        driver.get('https://www.google.com/')    # This website is protected against XSS so below payload will not generate alert
        time.sleep(3)

        google = Homepage(driver)
        time.sleep(5)
        google.enter_payload_google_textbox("<script>alert(1)</script>" + Keys.ENTER)
        time.sleep(3)
        try:
            obj = driver.switch_to.alert
            msg = obj.text
            print("Alert shows following msg:" + msg)
            with open('description_for_xss.yml') as file:
                info = yaml.load(file)
                print(info)
        except UnexpectedAlertPresentException:
            print("Excetional Alert is present")
        except NoAlertPresentException:
            print("Site is safe from XSS")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/pravinshinde/Documents/Project/Automated_Project/reports'))