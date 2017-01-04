import unittest
from selenium import webdriver

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

        self.driver.get('http://desktop-ng-test.fastlaneams.com/')

    def tearDown(self):
        self.driver.quit()