import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Function to initialize the driver
def create_driver():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    return driver

# Grouping tests using "describe" equivalent
def describe_login_tests():
    
    # Test 1: Valid login test
    def it_should_login_successfully():
        driver = create_driver()
        print("testing started")
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        
        # Perform login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        sleep(5)
        
        # Assert successful login
        text = driver.find_element(By.CLASS_NAME, "title").text 
        assert "products" in text.lower()
        print("TEST PASSED: LOGIN SUCCESSFUL")
        driver.quit()

    # Run the individual test cases
    it_should_login_successfully()

# Run the "describe" block
describe_login_tests()

