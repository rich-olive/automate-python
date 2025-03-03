import gspread

gc = gspread.service_account('service_account_credentials.json')

# interacting with a pre-existing gsheet
spreadsheet = gc.open("gspread101")
# this spreadsheet object has an attribute called 'sheet1'
ws = spreadsheet.sheet1
ws.update_acell('A1', 'Hello Google Sheets!')

# gspread auto saves and closes

# ws.update([["Hello", "world"]], "A3:B1")

# 1. To update a single cell in a Google Sheets spreadsheet:
# wks.update_acell(‘A1’, ‘Hello world!’).
# 2. To update method to update a range of cells:
# wks.update([["Hello", "world"]], "A2:B1")
# note that the values passed to the first argument must now be in the form of a 2D list
# (one or more lists inside another list)