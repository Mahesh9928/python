from selenium import webdriver
import time

# Set up the WebDriver (for Chrome)
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.com")
    
    # Wait for 5 seconds to keep the page open
    time.sleep(5)
    
finally:
    # Close the browser window automatically
    driver.quit()
