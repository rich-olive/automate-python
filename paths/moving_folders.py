from pathlib import Path
import shutil

src = Path.home() / "documents" / "python_automation" / "copying_stuff" / "fun_with_folders" / "my_3rd_folder" / "my_4th_folder"
dest = Path.home() / "documents" / "python_automation" / "moving_and_renaming" / "my_4th_folder"


shutil.move(src, dest)
# moved my_4th_folder to moving_and_renaming
# also moved my_5th_folder which was nested inside