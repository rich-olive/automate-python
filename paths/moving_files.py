from pathlib import Path
import shutil

new_folder = Path.home() / "documents" / "python_automation" / "moving_and_renaming"
new_folder.mkdir(exist_ok=True)

src = Path.home() / "documents" / "python_automation" / "copying_stuff" / "olive.txt"
# dest = Path.home() / "documents" / "python_automation" / "moving_and_renaming" / "olive.txt"
dest = new_folder / "olive.txt"
# must have the file name at the end of the destination path

if src.exists():
    shutil.move(src, dest)

with open(dest, "r") as file:
    print(file.read())

# I've combined a few different lessons here to create a directory, then move a file from one dir to the new one.