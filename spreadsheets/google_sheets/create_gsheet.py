import gspread

gc = gspread.service_account(r"C:\Users\olivi\Desktop\Google Credentials\service_account_credentials.json")



# creating with a new gsheet
new_spreadsheet = gc.create("gspread 561")
# creates a new spreadsheet object

new_spreadsheet.share("oliviam.richmond@gmail.com", perm_type="user", role="writer")