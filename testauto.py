import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestNavbarLinks(unittest.TestCase):

    def setUp(self):
        # Set up the browser (Chrome or Firefox)
        self.driver = webdriver.Chrome()  # or webdriver.Firefox() if using Firefox
        self.driver.implicitly_wait(20)  # Optional: Wait up to 10 seconds for elements to appear

    def test_navbar_links(self):
        driver = self.driver
        # Navigate to the webpage
        driver.get("https://pf.com.pk/")

        # Wait for the navbar element to be present
        navbar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "header"))
        )
        self.assertIsNotNone(navbar, "Navbar is not found on the page")

        # Get all the links in the navbar
        nav_links = navbar.find_elements(By.TAG_NAME, "a")
        self.assertGreater(len(nav_links), 0, "No links found in the navbar")

        # Create a dictionary of expected link text and corresponding URLs
        expected_links = {
            "About Us":"https://pf.com.pk/about-us/",
            "Careers":"https://pf.com.pk/career/",
            "Life at PF":"https://pf.com.pk/life-at-pf/",
            "Expertise":"https://pf.com.pk/expertise/",
            "Graduate Gateway Program":"https://pf.com.pk/trainee-program/",  
            # Add more links as needed
        }

        # Loop through each link, click, and verify the page navigation
        for link in nav_links:
            link_text = link.text.strip()  # Use strip to remove extra spaces in link text
            self.assertIn(link_text, expected_links, f"Unexpected link text '{link_text}' found in navbar")

            # Click the link and wait for the page to load
            link.click()

            # Wait until the new page's URL is the expected one
            WebDriverWait(driver, 10).until(EC.url_to_be(expected_links[link_text]))
            self.assertEqual(driver.current_url, expected_links[link_text], f"Failed to navigate to {expected_links[link_text]}")

            # Navigate back to the original page after each click
            driver.back()

            # Wait for the navbar to be present again after navigating back
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "header"))
            )

    def tearDown(self):
        # Tear down the browser after the test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
