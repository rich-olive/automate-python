# copying folders is very similar to copying files
# however, both source path and destination paths are now folders

from pathlib import Path
import shutil

src = Path.home() / "documents" / "python_automation" / "fun_with_folders"
dest = Path.home() / "documents" / "python_automation" / "copying_stuff" / "fun_with_folders"

# have to include / "fun_with_folders" at the end of the destination path

shutil.copytree(src, dest, dirs_exist_ok=True)
# it worked, and it added the nested folders (my_3rd/my_4th/my_5th)
# copy tree copies recursively (it copies everything inside)

# if we run again, it throws an error
# can add dirs_exist keyword
# added text file to original fun_with_folders
# ran again and now the file is in copying_stuff
