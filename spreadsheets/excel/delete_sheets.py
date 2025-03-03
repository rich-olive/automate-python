import openpyxl
import re

wb = openpyxl.load_workbook("Employees.xlsx")

regex = r"^Sheet\d+$"

ws_names = wb.sheetnames

print(ws_names)

for ws_name in ws_names:
    if re.search(regex, ws_name) is not None:
        del wb[ws_name]

wb.save("Employees.xlsx")