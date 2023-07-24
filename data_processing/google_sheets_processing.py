import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def read_links_from_google_sheets(sheet_name, credentials_file, sheet_key):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(creds)
    
    sheet = client.open_by_key(sheet_key).worksheet(sheet_name)
    data = sheet.get_all_records()

    links = [record['Link'] for record in data if 'Link' in record]

    return links

def add_youtube_link_back(sheet_name, credentials_file, sheet_key, video_url, i):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(creds)
    
    sheet = client.open_by_key(sheet_key).worksheet(sheet_name)
    sheet.update_cell(i, "Youtube Links", video_url)
    
