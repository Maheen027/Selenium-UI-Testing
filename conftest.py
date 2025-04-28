import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Or Firefox
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
