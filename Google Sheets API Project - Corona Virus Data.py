import gspread
from oauth2client.service_account import ServiceAccountCredentials

from pprint import pprint


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("API Google Sheets - Corona Virus Data Key.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Corona Virus Data U.S").sheet1

data = sheet.get_all_records()

row = sheet.row_values(4)
column = sheet.col_values(6)
cell = sheet.cell().value
insert_row = [", , , , , , "]
sheet.update_cell("")
sheet.insert_row()
sheet.delete_row()

pprint(f"{row}, {column}")


