from video_recording.video_recording import record_video
from video_editing.video_editing import edit_video
from data_processing.google_sheets_processing import read_links_from_google_sheets
from automated_browsing.auto_browse import automate_browsing
from youtube_upload.youtube_upload import upload_to_youtube
from threading import Thread
import os

def main():
    
    # Step 4: Data Processing - Read Links from Google Sheets
    sheet_name = "Sheet1"  # Name of the sheet in the Google Sheets document
    credentials_file = "credentials.json"  # Path to the JSON credentials file
    sheet_key = "1l7alNgUJJjW9yO6xSyH6Hqfd7GSqD0UnW4XC6x2Q1ng"  # Key of the Google Sheets document
    links = read_links_from_google_sheets(sheet_name, credentials_file, sheet_key)

    driver = automate_browsing(links)

    # Step 5: Automated Browsing (in a separate thread)
    # browsing_thread = Thread(target=automate_browsing, args=(links,))
    # browsing_thread.start()

    # Step 6: Video Recording
    video_file = "output.mp4"
    duration = 30  # Recording duration in seconds

    # Start the video recording (in the main thread)
    record_video_thread = Thread(target=record_video, args=(video_file, duration))
    record_video_thread.start()

    # Wait for both browsing and video recording to finish
    # browsing_thread.join()
    record_video_thread.join()

    # overlay_file = "overlay_video.mp4"
    # edited_file = "edited_video.mp4"
    # edit_video(video_file, overlay_file, edited_file)

    # video_file = "edited_video.mp4"
    # credentials_file = "credentials.json"
    # api_service_name = 'youtube'
    # api_version = 'v3'
    # video_id = upload_to_youtube(video_file, credentials_file, api_service_name, api_version)
    # print(f"Video uploaded successfully! Video ID: {video_id}")

if __name__ == "__main__":
    main()