# iterate over file paths
# crucial for dealing with multiple files
# carrying out batch operations on multiple files
# iterdir generates an iterator for files & folders within a directory
# iterate over each item one at a time
# each item is a pathlib path object
# so we have access to useful methods

# going to iterate over the files in the automate python folder
# locate the folder using pathlib

from pathlib import Path
from datetime import datetime

home = Path.home()
doc_path = home / 'PycharmProjects' / 'automate_python'

# with open(doc_path/'poem.txt', 'r') as file:
#     print(file.read())

path = Path.home() / 'PycharmProjects' / 'automate_python'

# for item in path.iterdir():
#     print(item)
# this loop will iterate through each item in the directory contained in our path variable

# C:\Users\olivi\PycharmProjects\automate_python\.git
# C:\Users\olivi\PycharmProjects\automate_python\.idea
# C:\Users\olivi\PycharmProjects\automate_python\.venv
# C:\Users\olivi\PycharmProjects\automate_python\absolute_paths.py
# C:\Users\olivi\PycharmProjects\automate_python\absolute_v_relative
# C:\Users\olivi\PycharmProjects\automate_python\append.py
# C:\Users\olivi\PycharmProjects\automate_python\csv_reader.py
# C:\Users\olivi\PycharmProjects\automate_python\csv_writer.py
# C:\Users\olivi\PycharmProjects\automate_python\dad_jokes.csv
# C:\Users\olivi\PycharmProjects\automate_python\dictionaries.py
# C:\Users\olivi\PycharmProjects\automate_python\joke_ratings_starter.py
# C:\Users\olivi\PycharmProjects\automate_python\mod_jokes.csv
# C:\Users\olivi\PycharmProjects\automate_python\paths
# C:\Users\olivi\PycharmProjects\automate_python\pets_and_more_treats.csv
# C:\Users\olivi\PycharmProjects\automate_python\pets_and_treats.csv
# C:\Users\olivi\PycharmProjects\automate_python\pets_and_treats.txt
# C:\Users\olivi\PycharmProjects\automate_python\poem.txt
# C:\Users\olivi\PycharmProjects\automate_python\product_sales.txt
# C:\Users\olivi\PycharmProjects\automate_python\product_sales_data.csv
# C:\Users\olivi\PycharmProjects\automate_python\product_sales_project.py
# C:\Users\olivi\PycharmProjects\automate_python\read.py
# C:\Users\olivi\PycharmProjects\automate_python\README.md
# C:\Users\olivi\PycharmProjects\automate_python\refactored_product_sales_data.csv
# C:\Users\olivi\PycharmProjects\automate_python\refactored_product_sales_project.py
# C:\Users\olivi\PycharmProjects\automate_python\relative_paths.py
# C:\Users\olivi\PycharmProjects\automate_python\test.txt
# C:\Users\olivi\PycharmProjects\automate_python\write.py


# we can use is_file() or is_dir() to only print the files if they are a file/folder
# for item in path.iterdir():
#     if item.is_file():
#         print(item.name, 'is a file')
#
# for item in path.iterdir():
#     if item.is_dir():
#         print(item.name, 'is a directory')

# notice that we target the item name using item.name!

# can use .suffix to target files of a certain type
for item in path.iterdir():
    if item.is_file() and item.suffix == '.txt':
        print(item)

# C:\Users\olivi\PycharmProjects\automate_python\pets_and_treats.txt
# C:\Users\olivi\PycharmProjects\automate_python\poem.txt
# C:\Users\olivi\PycharmProjects\automate_python\product_sales.txt
# C:\Users\olivi\PycharmProjects\automate_python\test.txt

# the same logic essentially
for item in path.iterdir():
    if item.suffix == '.txt':
        print(item)

# all of these items are Path objects, hence they have access to methods and attributes contained within that class
# like with Java, we can check the documentation to understand what exactly is available on the Path class
# presumably, there is a name attribute, hence we can access item.name
# same for suffix attribute
# and for the stem attribute

for item in path.iterdir():
    if item.suffix == '.csv':
        print(item.stem, ' is a .csv file') # no space required between comma

# now we only get the actual file name (the stem)

# can use 'in' to target a certain sequence of characters in a file
for item in path.iterdir():
    if 'read' in item.name.lower():
        print(item.stem, 'contains the word read')
# csv_reader contains the word read
# read contains the word read
# README contains the word read

# we can replace the print statements with logic
# e.g. we could read every file

# stat method to access key info such as size in bytes and date of last modification

print("***STAT***")
for item in path.iterdir():
    if item.is_file() and item.suffix == ".txt":
        print(item.stem, "is a text file")

        stats = item.stat()

        print('Size:', stats.st_size, 'bytes')
        print('Last modified:', stats.st_mtime)
        print('Last modified:', datetime.fromtimestamp(stats.st_mtime))
        # Size: 28 bytes
        # Last modified: 1739534621.7142334
        # seconds since 1 January 1970
