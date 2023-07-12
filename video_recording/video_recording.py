import cv2
import numpy as np
import pyautogui
import time
from PIL import Image
from io import BytesIO

def record_video(video_file, driver, duration):
    screen_width, screen_height = pyautogui.size()
    out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*"mp4v"), 30.0, (screen_width, screen_height))

    start_time = time.time()
    start_time = time.time()
    while time.time() - start_time < duration:
        # Capture the screen frame
        screenshot = driver.get_screenshot_as_png()
        img = Image.open(BytesIO(screenshot))
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Write the frame to the output file
        out.write(frame)

    # Release the video writer
    out.release()

