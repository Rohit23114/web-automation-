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
def describe_cart_tests():
    
    # Test 1: Testing add to cart
    def it_should_add_to_cart():
        driver = create_driver()
        print("testing add to cart")
        driver.get("https://www.saucedemo.com/")
        sleep(3)

        # Find all add to cart buttons and click the first 3
        add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for btn in add_to_cart_btns[:3]:
            btn.click()
        
        # Check if the cart badge reflects the added items
        cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert "3" in cart_value.text
        print("TEST PASSED: ADD TO CART")
        
        driver.quit()

    # Test 2: Testing remove from cart
    def it_should_remove_from_cart():
        driver = create_driver()
        print("testing remove from cart")
        driver.get("https://www.saucedemo.com/")
        sleep(3)

        # Find all add to cart buttons and click the first 3 items
        add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for btn in add_to_cart_btns[:3]:
            btn.click()
        
        # Now remove 2 items
        remove_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for btn in remove_btns[:2]:
            btn.click()
        
        # Check if the cart badge reflects the removed items
        cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert "1" in cart_value.text
        print("TEST PASSED: REMOVE FROM CART")

        driver.quit()

    # Run the individual test cases
    it_should_add_to_cart()
    it_should_remove_from_cart()

# Run the "describe" block
describe_cart_tests()
