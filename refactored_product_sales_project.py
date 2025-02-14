import csv
import datetime

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

meaningful_sales_data = []

with open("product_sales.txt", "r") as product_sales_file:
    product_sales_content = product_sales_file.readlines()

    for index, row in enumerate(product_sales_content):
        current_date = datetime.date.today()
        sale_id = index+1
        product_id = row.strip()
        product_name = str(product_data[row.strip()]["product_name"]),
        unit_price = product_data[row.strip()]["unit_price"]

        meaningful_sales_data.append([current_date, sale_id, product_id, product_name, unit_price])

print(meaningful_sales_data)

with open("refactored_product_sales_data.csv", "w", newline="") as output:
    data_write_object = csv.writer(output)
    data_write_object.writerow(["current_date", "sale_id", "product_id", "name", "price"])
    data_write_object.writerows(meaningful_sales_data)
