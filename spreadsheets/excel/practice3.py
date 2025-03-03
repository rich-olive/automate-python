import openpyxl

wb = openpyxl.load_workbook("Automating Worksheets.xlsx")

ws_names = wb.sheetnames

print(ws_names)