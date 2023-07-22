import cv2
import numpy as np
import pyautogui
import time


def record_video(video_file, duration):
    screen_width, screen_height = pyautogui.size()
    out = cv2.VideoWriter(video_file, cv2.VideoWriter.fourcc(*"mp4v"), 30.0, (screen_width, screen_height),True)

    start_time = cv2.getTickCount()
    while (cv2.getTickCount() - start_time) / cv2.getTickFrequency() < duration:
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        out.write(frame)
        
    out.release()
    