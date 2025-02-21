 # ["Freddie", "dog", "frozen peas"]
 # ["Henny", "dog", "cheese"]
 # ["Bette", "dog", "dog peen"]
 # ["Dead", "fish", "raw mince meat"]
 # ["Spike", "bird", "sunflower seeds"]

import csv

# .csv creates an excel file
# .txt creates a plaintext file with values separated by commas
with open("pets_and_more_treats.csv", "w", newline="") as csv_file:
    # set to "w" for write
    # the newline="" ensures there isn't a blank row after the header
    csv_writer = csv.writer(csv_file)
    # calling the .writer method from the csv module
    csv_writer.writerow(["Name", "Species", "Favourite Treat"])
    # sets the header
    # it's not essential but it is good practice

    # writerow(): adds row in the form of a list one at a time
    # csv_writer.writerow(["Freddie", "dog", "frozen peas"])
    # csv_writer.writerow(["Henny", "dog", "cheese"])
    # csv_writer.writerow(["Bette", "dog", "dog peen"])

    # writerows(): adds multiple rows: accepts a list of lists as an argument
    csv_writer.writerows([["Freddie", "dog", "frozen peas"],
                          ["Henny", "dog", "cheese"],
                          ["Bette", "dog", "dog peen"],
                          ["Dead", "fish", "raw mince meat"],
                          ["Spike", "bird", "sunflower seeds"]])

    # we are converting simple list data to excel spreadsheets!
    # we don't see any duplicates because we are in "w" write mode! this overwrites any previous data