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

# def find_named_range_column(sheet_name, credentials_file, sheet_key, named_range_name):
#     scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#     creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
#     client = gspread.authorize(creds)

#     sheet = client.open_by_key(sheet_key).worksheet(sheet_name)
#     named_range = sheet.get(named_range_name, value_render_option="UNFORMATTED_VALUE")

#     if named_range is None:
#         return None

#     range_a1 = named_range.range
#     named_range.index


def add_youtube_link_back(sheet_name, credentials_file, sheet_key, video_url, i, column_number_input):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(creds)
    
    sheet = client.open_by_key(sheet_key).worksheet(sheet_name)
    column_number = column_number_input
    
    if column_number is None:
        print("Named range 'Youtube Links' not found in the sheet.")
        return

    sheet.update_cell(i, column_number, video_url)

    
