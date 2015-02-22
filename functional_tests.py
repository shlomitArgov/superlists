__author__ = 'Shlomit'
import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_todo_list(self):
        
        # Edith has heard about a cool new to-do lists  app.
        # She goes to its homepage
        self.browser.get('http://localhost:8000')
        self.assertIn('Django', self.browser.title)

        # Edith notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)




if __name__ == '__main__':
    unittest.main()