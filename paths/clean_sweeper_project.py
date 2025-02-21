from pathlib import Path
import shutil

# "C:\Users\olivi\Desktop\clean_sweep_project"

# user specify a directory path
user_input = input("Enter a path\n")
# validate
user_defined_path = Path(user_input)
closet_directory = user_defined_path / "closet"
text_files = closet_directory / "text_files"
csv = closet_directory / "csv_files"
folders = closet_directory / "folders"
# create new directory ("closet") within user-specified dir
# mkdir
if user_defined_path.exists():
    closet_directory.mkdir(exist_ok=True)
    text_files.mkdir(exist_ok=True)
    csv.mkdir(exist_ok=True)
    folders.mkdir(exist_ok=True)
    print("folder exists")
else:
    print("folder doesn't exist")
#     closet_directory = path / "closet"
#
#     closet_directory.mkdir(exist_ok=True)
#
# # create 3 more sub directories
# # text_files
# # csv_files
# # folders
#     text_files = closet_directory / "text_files"
#     csv = closet_directory / "csv_files"
#     folders = closet_directory / "folders"


# src = Path.home() / "documents" / "python_automation" / "copying_stuff" / "olive.txt"
# dest = Path.home() / "documents" / "python_automation" / "moving_and_renaming" / "olive.txt"



# iterate over the user-specified directory
for item in closet_directory.iterdir():
    # if "closet" in item:
    #     continue
    if item.suffix == ".txt":
        src = closet_directory
        dest = closet_directory / text_files
        if src.exists():
            shutil.move(src, dest)

# ensure to exclude the 'closet' directory
# check if file is .txt or .csv
# move into the 'text_files' or 'csv_files' directories
# delete any directory with 'temp' in the name
# if a directory doesn't have 'temp' in the name, move to 'folders' directory
# any remaining files should be moved to the 'closet' directory

## more specific conditions should come before general ones so they are not swept up
# once script has finished, print "folder cleanup complete!"