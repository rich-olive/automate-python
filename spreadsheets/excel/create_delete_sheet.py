import openpyxl

wb = openpyxl.load_workbook("Automating Worksheets.xlsx")

# CREATE NEW WORKSHEET
wb.create_sheet("Monthly Outgoings")

# DELETE WORKSHEET
del wb["Sheet2"]

wb.save("Automating Worksheets.xlsx")

# Result is now 3 sheets: Olivia's Finances, Utility Bills, Monthly Outgoings