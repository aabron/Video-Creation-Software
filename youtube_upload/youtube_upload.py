import os
from googleapiclient.discovery import build
from google.oauth2 import service_account

def upload_to_youtube(video_file, credentials_file, api_service_name, api_version):
    # Load credentials
    credentials = service_account.Credentials.from_service_account_file(
        credentials_file, scopes=['https://www.googleapis.com/auth/youtube.upload']
    )

    # Create a YouTube API client
    youtube = build(api_service_name, api_version, credentials=credentials)

    # Upload the video
    request_body = {
        'snippet': {
            'title': 'My Uploaded Video',
            'description': 'Description of my video',
            'tags': ['tag1', 'tag2']
        },
        'status': {
            'privacyStatus': 'public'
        }
    }

    response = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=video_file
    ).execute()

    video_id = response['id']
    return video_id
