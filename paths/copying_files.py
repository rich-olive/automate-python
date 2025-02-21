# shutil module
# utility tool that offers high-level operations for handling files & collections of files
# functions for copying, moving, renaming and deleting files
# and for working with file archives

from pathlib import Path
import shutil


# home, pycharm, automate, dadjokes.
# src path, destination path

# when copying files, the source path is a file
# the destination path is a folder

src = Path.home() / "PycharmProjects" / "automate_python" / "shutil_test_file.txt"
dest = Path.home() / "documents" / "python_automation" / "copying_stuff"
dest_file_path = dest / "shutil_test_file.txt"

if not src.exists():
    print(src, "does not exist")
elif dest_file_path.exists():
    print("the file already exists in the destination folder")
else:
    print("copying")
    shutil.copy(src, dest)
# copies to new destination

# if source doesn't exist, we'll get an error
# if there is a file with the same name in the destination folder, this method will overwrite it