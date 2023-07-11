import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def read_links_from_google_sheets(sheet_name, credentials_file, sheet_key):
    # load Google Sheets credentials
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(creds)

    # open the specified Google Sheet
    sheet = client.open_by_key(sheet_key).worksheet(sheet_name)

    # read data from the sheet
    data = sheet.get_all_records()

    # extract the links from the data
    links = [record['Link'] for record in data if 'Link' in record]

    return links
