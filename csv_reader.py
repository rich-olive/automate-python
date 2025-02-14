import csv

with open("dad_jokes.csv", "r") as csv_file:
    # csv.reader is a method in the csv module: we pass our file variable as an argument
    csv_reader = csv.reader(csv_file)

    # we can read data from the csv file by iterating over the rows
    # each row returned will be a list of strings
    # each string represents a field/cell
    # the for loop will iterate once for each row in the file
    next(csv_reader)
    for row in csv_reader:
        print(row)
            # joke_id = row[0]
            # joke = row[1]
            # joke_rating = row[2]
            # print(f"Joke number {joke_id}: {joke}. The rating of this joke is {joke_rating}")
# for the jokes csv, each row has 3 values: joke ID, joke, joke rating
# CSV files often have a header row (cell headers)
# currently: Joke number ï»¿ID: Joke. The rating of this joke is Rating
# we don't want to print this
# there is an inbuilt function: next()
# this skips the first row
# next(csv_reader)