from pathlib import Path
import shutil

src = Path.home() / "documents" / "python_automation" / "moving_and_renaming" / "my_4th_folder"
dest = Path.home() / "documents" / "python_automation" / "moving_and_renaming" / "my_fourth_folder"

if src.exists():
    shutil.move(src, dest)