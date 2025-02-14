import csv
import datetime

# 1. Reads a text file containing a list of product IDs signifying product sales transactions.
# 2. Uses that data to generate a CSV file containing the following data points associated with each transaction:
    # a. A sequential ID indicating the order of the individual transaction within the file.
    # b. The date on which the file was generated.
    # c. The product ID
    # d. The product name
    # e. The product unit price

# Product ID  Product Name            Unit Price
# P001        Wireless Headphones     100
# P002        Laptop Backpack         60
# P003        Bluetooth Speaker       50
# P004        USB Flash Drive         20
# P005        Mobile Phone Case       15
# P006        Wireless Mouse          30
# P007        Laptop Stand            40
# P008        HDMI Cable              15

product_data = {
    "P001": {"product_name": "Wireless Headphones",
     "unit_price": 100},
    "P002": {"product_name": "Laptop Backpack",
     "unit_price": 60},
    "P003": {"product_name": "Bluetooth Speaker",
             "unit_price": 50},
    "P004": {"product_name": "USB Flash Drive",
             "unit_price": 20},
    "P005": {"product_name": "Mobile Phone Case",
             "unit_price": 15},
    "P006": {"product_name": "Wireless Mouse",
             "unit_price": 30},
    "P007": {"product_name": "Laptop Stand",
             "unit_price": 40},
    "P008": {"product_name": "HDMI Cable",
             "unit_price": 15},
    "P009": {"product_name": "Smartphone",
             "unit_price": 600},
    "P010": {"product_name": "External Hard Drive",
             "unit_price": 100}
    }

# print(product_data)

# read the original CSV file
# with open("product_sales.txt", "r") as product_sales_file:
#     product_sales_content_all = product_sales_file.read()
#     product_sales_content = product_sales_file.readlines()
#     print(f"PRODUCT SALES CONTENT: \n{product_sales_content_all}")
#     # print(f"PRODUCT SALES CONTENT LENGTH: \n{len(product_sales_content)}") length of each character!
#     for line in product_sales_content:
#         print(line) # type string
    # print(f"length of each line? : {len(product_sales_content)}") # 1000, seems accurate given the number of prod codes in the txt file

    # print(type(product_sales_content_all))

# convert each entry (in format P007, P002, P001, etc) into the actual product name
# so we have 10 products.
# we could use the prod code (which is what we have access to!)
# to map to the product name in the dictionary
# need somewhere to store this data

# product_names = []

meaningful_sales_data = []

with open("product_sales.txt", "r") as product_sales_file:
    product_sales_content = product_sales_file.readlines()

    for index, row in enumerate(product_sales_content):
        # added this line to reduce duplicate code and make it clearer that i'm stripping the row whitespace
        row = row.strip()
        # probably clearer to save each into a temp var and then append
        current_date = datetime.date.today()
        # sale_id = 1 #dummy data for now
        sale_id = index+1
        # this and enumerate works nicely for creating a sequential sale id
        # product_id = row.strip()
        # product_name = str(product_data[row.strip()]["product_name"]),
        # unit_price = product_data[row.strip()]["unit_price"]

        product_id = row
        product_name = product_data[row]["product_name"]
        unit_price = product_data[row]["unit_price"]

        meaningful_sales_data.append([current_date, sale_id, product_id, product_name, unit_price])
        # current date not correctly formatted- if I manually change the format on excel, it does show today's date...
        # product name showing in a strange format... type shows it is a string...


        # meaningful_sales_data.append([row.strip(), product_data[row.strip()]["product_name"], product_data[row.strip()]["unit_price"]])
        # [['P005', 'Mobile Phone Case', 15], ['P001', 'Wireless Headphones', 100], ['P001', 'Wireless Headphones', 100]...]
        # meaningful_sales_data.append(product_data[row.strip()]["product_name"])
        # meaningful_sales_data.append(product_data[row.strip()]["unit_price"])
        # adding all thus: ['P005', 'Mobile Phone Case', 15, 'P001', 'Wireless Headphones', 100, 'P001', 'Wireless Headphones', 100, 'P006', 'Wireless Mouse', 30...]
        # so this would produce data all on the same row
        # so how to now create multiple lines
        # print(product_data[row.strip()]["product_name"])
        # product_names.append(product_data[row.strip()]["product_name"])

# print(product_names)
print(meaningful_sales_data)
# success!
# had to strip the whitespace/tabs as the error was showing "P005\n"
# checked against first & last few entries in the .txt file
# now saved to product_names list temporarily...

# save this to a variable!
# assign the actual product/unit price
# use the order of entries to create a 'sale_id' (when the item was purchased- sequential!)

# TEST OUTPUT
with open("product_sales_data.csv", "w", newline="") as output:
    data_write_object = csv.writer(output)
    data_write_object.writerow(["current_date", "sale_id", "product_id", "name", "price"])
    # added headers however, not quite right as we need to add the current date values and sale id values
    # prod_id (prod code: P001, etc) is next
    # then name and price
    data_write_object.writerows(meaningful_sales_data)
# this worked! there is the newline issue to deal with- add newline="" to the with statement
# need to add headers

# weird product name display issue
# product_name appearing in ('') when opening in excel file
# appending it directly seems to work ?? both return <class str>
# found the error!!
# i added a comma at the end of the product_name = product_data[row]["product_name"],
# python reads this comma as a tuple
# and the class was actually returning <tuple> when printing to the console
# hence why the direct add to the list was not producing ("Wireless Headphones")
# - the comma there did not affect adding things to the meaningful_data list
# it's probably a hangover from when the data was initially all added at once when i was building programme



# the format of the current date when opening excel file
# fixed by using f string with % format specifiers
# today_date = datetime.date.today()
# current_date = f"{today_date: %d-%m-%Y}"
# this creates the format 14-02-2025
#https://mathspp.com/blog/twitter-threads/datetime-objects-and-f-strings#:~:text=In%20Python%20%F0%9F%90%8D%2C%20the%20built,%3E%3E%3E%20now%20%3D%20dt.
# and see W3 schools
# i also created a variable to carry out this logic, and moved it outside of the for loop so that it doesn't
# need to run every time i run the loop/every iteration of the loop
# i refactored this further by eradicating the temporary today_date variable
# current_date = f"{datetime.date.today(): %d-%m-%Y}"
# though it might be CLEARER to use current_date with the datetime.date.today() logic
# and then reassign it to the formatted string
# current_date = datetime.date.today()
# current_date = f"{current_date: %d-%m-%Y}"
# i'll keep it like this!

# create a new CSV file with the headings
# current_date
# sale_id
# product_id
# name
# price

