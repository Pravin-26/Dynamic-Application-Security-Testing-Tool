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

class SQLTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome('/Users/pravinshinde/Documents/Project/Automated_Project/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def test_sql(self):
        driver = self.driver
        driver.get('http://pravin26.pythonanywhere.com/')
        time.sleep(3)

        sql = Homepage(driver)
        time.sleep(3)
        sql.enter_sqlpayload_textbox_name("' OR '1")
        time.sleep(3)
        sql.enter_sqlpayload_textbox_password("' OR '1" + Keys.ENTER)
        time.sleep(4)

        with open("description_for_sql.yml", 'r') as file:
            info = yaml.load(file)
            print(info)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/pravinshinde/Documents/Project/Automated_Project/reports'))