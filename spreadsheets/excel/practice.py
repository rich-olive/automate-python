import openpyxl
book_data = [
    ["Title", "Author", "Genre"],
    ["The Rum Diary","Hunter S. Thompson","Fiction"],
    ["In Cold Blood", "Truman Capote", "True Crime"],
    ["East of Eden", "John Steinbeck", "Fiction"]
]
# create a new workbook
wb = openpyxl.Workbook()

# target the first sheet
wb.create_sheet("books")
books_sheet = wb["books"]
del wb["Sheet"]

# input some data
book_data_range = "A1:C" + str(len(book_data))
book_range = books_sheet[book_data_range]

for i in range(len(book_data)):
    row = book_data[i]
    for j in range(len(row)):
        val = row[j]

        book_range[i][j].value = val

wb.save('books.xlsx')


# this only creates the workbook 'in memory' - doesn't save it

