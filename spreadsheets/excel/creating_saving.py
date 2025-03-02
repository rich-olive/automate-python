import openpyxl

wb = openpyxl.Workbook()
# this only creates the workbook 'in memory' - doesn't save it

wb.save('my_workbook.xlsx')
# .save() takes one parameter: the name of the file (if we want to save it to same directory) or the path
# (to save elsewhere)

