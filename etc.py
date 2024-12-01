


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed

try:
    # Open Google
    driver.get("https://www.google.com")
    
    # Find the search bar and input the query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("etccollection.com")
    search_box.send_keys(Keys.RETURN)  # Press Enter to search
    
    # Wait to observe the search results
    time.sleep(5)  # Adjust the time if needed
    
finally:
    # Close the browser window automatically
    driver.quit()
