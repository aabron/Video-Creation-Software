from pyvirtualdisplay.smartdisplay import SmartDisplay
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

driver = None

def automate_browsing(links):
    global driver
    
    # Configure Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

    # Set path to your Chrome driver executable
    chrome_driver_path = r"C:\Users\8068programmer\Desktop\Projects\Extras\chromedriver.exe"

    # Initialize Chrome driver
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
    try:
        for link in links:
            # Open the Instagram link
            driver.get(link)

            # Simulate scrolling action
            scroll_element = driver.find_element(By.TAG_NAME, 'body')
            for _ in range(5):  # Scroll 5 times, adjust the number as needed
                scroll_element.send_keys(Keys.PAGE_DOWN)
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
                time.sleep(2)

    except NoSuchElementException as e:
        print("Element not found: ", e)

    finally:
        global browsing_complete
        browsing_complete = True
        # Quit the browser
        driver.quit()
        
    return driver
        
        
def isBrowsingComplete():
    return browsing_complete

