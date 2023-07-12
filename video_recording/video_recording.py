import cv2
import numpy as np
import pyautogui
import time
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from moviepy.editor import ImageSequenceClip


def record_video(video_file, duration):
    global driver
    
    # Configure Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

    # Set path to your Chrome driver executable
    chrome_driver_path = r"C:\Users\8068programmer\Desktop\Projects\Extras\chromedriver.exe"

    # Initialize Chrome driver
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
    
    screen_width, screen_height = pyautogui.size()
    fourcc = cv2.VideoWriter.fourcc("m","p","4","v",)
    out = cv2.VideoWriter(video_file, fourcc, 30.0, (1920, 1080),True)

    start_time = time.time()
    while time.time() - start_time < duration:
        # Capture the screen frame
        screenshot = driver.get_screenshot_as_png()
        frame = cv2.imdecode(np.frombuffer(screenshot, np.uint8), cv2.IMREAD_COLOR)

        # Write the frame to the output video file
        out.write(frame)

    # Release the VideoWriter object
    out.release()
