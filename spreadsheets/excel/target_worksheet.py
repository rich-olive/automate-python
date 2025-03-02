import openpyxl

wb = openpyxl.load_workbook("Automating Worksheets.xlsx")
# One workbook - several worksheets

# CAPTURE THE ACTIVE SHEET
active_ws = wb.active
print(active_ws.title)

# can also use bracket notation to 'capture' the worksheet
ws3 = wb["Sheet3"]
print(ws3.title) # Sheet3

# RENAME A WORKSHEET
ws3.title = "Utility Bills"

# MUST SAVE THE WORKBOOK AFTER ANY CHANGES
wb.save("Automating Worksheets.xlsx") # this has updated the workbook!