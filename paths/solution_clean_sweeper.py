from pathlib import Path
import shutil

# PATH
# C:\Users\olivi\Desktop\messy_folder

# use while loop to keep running the input() function until the user enters a valid path
while True:
    path = Path(input("Enter a path:\n"))
# directly convert user input into a path object
    if path.exists():
        break

    print("Invalid path.")

closet_dir = path / 'closet'
closet_dir.mkdir(exist_ok=True)

text_dir = closet_dir / 'text_files'
text_dir.mkdir(exist_ok=True)

csv_dir = closet_dir / 'csv_files'
csv_dir.mkdir(exist_ok=True)

folders_dir = closet_dir / 'folders'
folders_dir.mkdir(exist_ok=True)
# i had to move my mkdir code out of the if/else statement so it would be available to the for loop
# this is much cleaner

for item in path.iterdir():
    if item == closet_dir:
        print(item) # path object = path C:\Users\olivi\Desktop\messy_folder\closet
        print(item.name) # path object . name = "closet"
        continue
    # i struggled with skipping the closet folder
    # maybe because i was searching for a folder with "closet" in the name
    # this reminds me that item is actually a path object!
    # i learned this in the lessons but forgot by the time i did the project
    # hence why we have to use the .name attribute to display just the name of the file
    # so we are essentially comparing file paths!
    elif item.is_file() and item.suffix == ".txt":
        shutil.move(item, text_dir / item.name)
    # going back to the item = path object from above
    # here we are saying 'move this entire path into this other path'
    # so like the src/dest that i used
    # but much cleaner
    elif item.is_file() and item.suffix == '.csv':
        shutil.move(item, csv_dir / item.name)
    elif item.is_dir() and 'temp' in item.name:
        shutil.rmtree(item)
    elif item.is_dir():
        shutil.move(item, folders_dir / item.name)
    else:
        shutil.move(item, closet_dir / item.name)
    # i did consider using an else statement at the end of my for loop
    # to sweep up any other files
    # but i worried about unintentionally targeting a file...
    # it works though, i just need to ensure i consider edge cases in future
print('Folder cleanup complete!')