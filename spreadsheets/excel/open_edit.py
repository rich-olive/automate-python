import openpyxl

wb = openpyxl.load_workbook("my_workbook.xlsx")

# Worksheet
ws = wb.active

ws["A1"] = "Hello Excel"

# we have to save the file for the changes to persist
wb.save("my_workbook.xlsx")

# openpyxl auto closes files