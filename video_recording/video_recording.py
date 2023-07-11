import cv2
import pyautogui
import numpy as np

def record_video(output_file, duration):
    screen_width, screen_height = pyautogui.size()
    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (screen_width, screen_height))

    # Start recording
    start_time = pyautogui.time()
    while pyautogui.time() - start_time < duration:
        # Capture the screen frame
        img = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Write the frame to the video file
        out.write(frame)

    # Release the video writer and close the output file
    out.release()
    cv2.destroyAllWindows()

# Usage example
output_file = "output.avi"
duration = 10  # Recording duration in seconds
record_video(output_file, duration)
