import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# Function to initialize the driver
def create_driver():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    return driver

# Grouping tests using "describe" equivalent
def describe_testing():
    
    # Test 1: Opening the website and checking the title
    def it_should_display_correct_title():
        driver = create_driver()
        print("testing started")
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        title = driver.title
        assert "Swag Labs" in title
        print("TEST 0: `title` test passed")
        driver.quit()

    # Running the individual test cases
    it_should_display_correct_title()
    
# Running the "describe" block
describe_testing()


