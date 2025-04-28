import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://pf.com.pk/")
        self.assertIn("Programmers Force", driver.title)
        
        #elem = driver.find_element(By.NAME, "q")
        #elem.send_keys("pycon")
        #elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)





import time
def tearDown(self):
         time.sleep(30)  # Pause for 5 seconds before closing the browser
         self.driver.close()

if __name__ == "__main__":
    unittest.main()
