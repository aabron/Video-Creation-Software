from pyvirtualdisplay.smartdisplay import SmartDisplay
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import random

driver = None

def automate_browsing(links, duration, chosen_scroll_option):
    global driver
    
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    chrome_driver_path = "chromedriver.exe"

    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
    
    try:
    
        driver.get(links)

        last_height = driver.execute_script("return document.body.scrollHeight")

        start_time = time.time()
        if chosen_scroll_option == "Scroll Up and Down":
            while time.time() - start_time < duration:
                driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
                time.sleep(4)
                driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});")
                time.sleep(4)

        elif chosen_scroll_option == "Scroll halfway down wait, click on post, wait, go back, scroll up":
            while time.time() - start_time < duration:
                driver.execute_script("window.scrollTo({top: (document.body.scrollHeight)/2, behavior: 'smooth'});")
                time.sleep(4)
                try:
                    post_divs = driver.find_elements(By.CSS_SELECTOR, "div.v1Nh3 a")
                    visible_posts = [post for post in post_divs if post.is_displayed()]

                    if visible_posts:
                        random_post = random.choice(visible_posts)
                        random_post.click()
                        time.sleep(4)
                        driver.back()
                        time.sleep(4)
                        driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});")

                except NoSuchElementException as e:
                    print("Element not found: ", e)

        elif chosen_scroll_option == "Scroll down wait, scroll up halfway, click post, wait, go back scroll up":
            while time.time() - start_time < duration:
                driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
                time.sleep(4)
                driver.execute_script("window.scrollTo({top: document.body.scrollHeight/2, behavior: 'smooth'});")
                time.sleep(4)
                try:
                    # post = WebDriverWait(driver, duration).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.v1Nh3 a")))
                    # post.click()
                    time.sleep(4)
                    driver.back()
                    time.sleep(4)
                    driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});")
                except NoSuchElementException as e:
                    print("Element not found: ", e)
                     
    except NoSuchElementException as e:
        print("Element not found: ", e)

    finally:
        driver.quit

    return driver
