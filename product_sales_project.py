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
}


print(product_data)

# read the original CSV file
# convert each entry (in format P007, P002, P001, etc) into the actual product name
# save this to a variable!
# assign the actual product/unit price
# use the order of entries to create a 'sale_id' (when the item was purchased- sequential!)

# create a new CSV file with the headings
# current_date
# sale_id
# product_id
# name
# price

