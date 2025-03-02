import openpyxl

wb = openpyxl.load_workbook("Employees.xlsx")

# cycle through list of employees
# create sheet for each
# delete any sheet with 'Sheet' followed by a digit

employees = ["John Smith", "Amit Patel", "Robert Brown", "Sanaa Al Farsi", "Michael Miller", "Chiamaka Mbah", "Maria Rodriguez", "David Clark", "Chen Wei"]

for employee in employees:
    wb.create_sheet(employee)

wb.save("Employees.xlsx")