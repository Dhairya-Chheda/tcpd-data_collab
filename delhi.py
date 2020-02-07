from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive","https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', SCOPES)
client = gspread.authorize(creds)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1q-xbFWn5ChMvKKIhoN-QbwQ1SS74c7FyJxYd5A25C8U'
BASIM_SPREADSHEET_ID = '1-XixyeURaPVrcslUFPkxI3txQgUDQeHPJYMxT9ALXho'

SAMPLE_RANGE_NAME = 'Copy of Delhi_Candidates_Caste_Data!O:V'
BASIM_RANGE_NAME = 'Delhi_Candidates_Caste_Data!O:V'

sheet = client.open("Delhi_Candidates_Caste_Data_Master").sheet1

list_of_hashes = sheet.get_all_records()
print(list_of_hashes)   
