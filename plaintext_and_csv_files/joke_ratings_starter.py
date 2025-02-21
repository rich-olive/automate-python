import csv

# import csv
# convert rating from string to int!
# simple if/elif/else logic to create the rating category



def rating_category(rating):
    rating = int(rating)

    if rating <= -3:
        category = 'abysmal'
    elif rating <= -1:
        category = 'awful'
    else:
        category = 'bad'

    return category

modified_jokes = []

with open("dad_jokes.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    # take a file object, return a reader object
    # then we have access to the methods on that reader object
    # csv_reader is the variable name
    # csv.reader() is the method from the csv module that creates the reader object
    # we pass in csv_file (which is actually 'dad_jokes.csv'
    # and save to csv_reader
    # now we can access all the methods on the reader object by calling them on the csv_reader variable name
    # for example the next() method for skipping rows
    # also able to iterate through the rows in the file by using a for loop

    # we don't want to add a rating category to the headers
    # but we do want to add the rating category HEADER to headers
    # next() returns a value (as well as skipping past the header row)
    # the value is a list containing values from that skipped row!
    headers = next(csv_reader)
    headers.append("rating_category")
    modified_jokes.append(headers)
    for row in csv_reader:
        row.append(rating_category(row[2]))

        modified_jokes.append(row)

with open("mod_jokes.csv", "w") as new_csv_file:
    csv_writer = csv.writer(new_csv_file)

    csv_writer.writerows(modified_jokes)


