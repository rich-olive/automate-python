import openpyxl

# top level of this data is the headers/column titles
data = [
    ["Product", "Category", "Price"],
    ["Apple iPhone 12", "Electronics", 799],
    ["Nike Air Force 1", "Footwear", 90],
    ["The Alchemist", "Books", 16.99],
    ["Instant Pot Duo", "Home & Kitchen", 89]
]

wb = openpyxl.load_workbook("products.xlsx")

ws = wb["Sheet1"]

# we often know the number of columns but not the number of rows
# hence we can dynamically add data with in an unknown number of rows

cell_range = "A1:C" + str(len(data)) # basically, the length of the data list, converted to a string
# so cell_range == A1:C5

rng = ws[cell_range]
# range is equal to Sheet1, A1 to C5

# print(rng)

# range generates a sequence of numbers to iterate over
# starts at zero and goes to the argument we feed it (len(data) minus one
for i in range(len(data)):
    row = data[i]
    print("We say hello to:", i, row)
    # this time iterating across the number of items in the row!
    for j in range(len(row)):
        val = row[j]
        print("In this row is:", j, val)
        print(row[j]) # val == row[j] == data[i][j]
        print(data[i][j])
        rng[i][j].value = val

# i = 0: ['Product', 'Category', 'Price']
# j = 0: "Product"
# j = 1: "Category"
# j = 2: "Price"
# i = 1: ['Apple iPhone 12', 'Electronics', 799]
# j = 0: "Apple iPhone 12"
# j = 1: "Electronics"
# j = 2: 799



wb.save("products.xlsx")