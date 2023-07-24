import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

def authenticate_youtube(credentials_file):
    
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        credentials_file, ['https://www.googleapis.com/auth/youtube.upload']
    )
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=credentials)

    return youtube


def upload_to_youtube(video_file, youtube, title, description):
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': ['your', 'tags', 'here'],
            'categoryId': '22'  
        },
        'status': {
            'privacyStatus': 'private'  
        }
    }

    # Upload the video
    try:
        response = youtube.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=video_file
        ).execute()

        video_id = response['id']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        print(f'Video uploaded successfully! Video ID: {video_id}')
        return video_url

    except googleapiclient.errors.HttpError as e:
        print(f'An error occurred while uploading the video: {e}')
        return None