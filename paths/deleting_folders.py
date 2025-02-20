from pathlib import Path
import shutil

p = Path.home() / "documents" / "python_automation" /  "doomed_folder"

if p.exists():
    p.rmdir()
# remove directory
# on run, it deleted the "doomed_folder" directory


p2 = Path.home() / "documents" / "python_automation" /  "doomed_folder_two"

# if p2.exists():
#     p2.rmdir()
# attempting to remove a folder which is not empty
# on run: OSError: [WinError 145] The directory is not empty: 'C:\\Users\\olivi\\documents\\python_automation\\doomed_folder_two'

# instead, use rmtree from shutil- deletes everything inside of doomed_folder_two!!
# this deletes recursively
# be very careful - do not delete documents folder!

if p2.exists():
    shutil.rmtree(p2)