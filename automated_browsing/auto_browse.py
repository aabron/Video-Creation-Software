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

def automate_browsing(links, duration):
    global driver
    
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    chrome_driver_path = r"C:\Users\8068programmer\Desktop\Projects\Extras\chromedriver.exe"

    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
    
    try:
    
        driver.get(links)

        last_height = driver.execute_script("return document.body.scrollHeight")

        start_time = time.time()
        
        while time.time() - start_time < duration:
            driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
            time.sleep(4)
            
            driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});")
            time.sleep(4)
            
            new_height = driver.execute_script("return document.body.scrollHeight")
            
            # if new_height == last_height:
            #     break
            
            # last_height = new_height

    except NoSuchElementException as e:
        print("Element not found: ", e)

    finally:
        driver.quit

    return driver
