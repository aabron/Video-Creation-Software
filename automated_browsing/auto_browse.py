from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from data_processing.google_sheets_processing import read_links_from_google_sheets

# set the path to your chromedriver executable
webdriver_service = Service('path_to_chromedriver')  # replace 'path_to_chromedriver' with the actual path

def automate_browsing(sheet_name, credentials_file, sheet_key):
    # read links from Google Sheets
    links = read_links_from_google_sheets(sheet_name, credentials_file, sheet_key)

    # start the ChromeDriver
    driver = webdriver.Chrome(service=webdriver_service)

    for link in links:
        # open the Instagram link
        driver.get(link)

        # simulate scrolling action
        scroll_element = driver.find_element(By.TAG_NAME, 'body')
        for _ in range(5):  # Scroll 5 times, adjust the number as needed
            scroll_element.send_keys(Keys.PAGE_DOWN)
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # close the browser
    driver.quit()
