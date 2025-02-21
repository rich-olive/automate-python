from pathlib import Path
import shutil

# src = Path.home() / "documents" / "python_automation" / "moving_and_renaming" / "olive.txt"
# dest = Path.home() / "documents" / "python_automation" / "moving_and_renaming" / "olivia.txt"

# MOVING AND RENAMING
src = Path.home() / "documents" / "python_automation" / "moving_and_renaming" / "olivia.txt"
dest = Path.home() / "documents" / "python_automation" / "moving_and_renaming" / "my_fourth_folder" / "molivia.txt"

if src.exists():
    shutil.move(src, dest)

# to rename, basically just move the file to the same location and give it a new name
# e.g. same path / olive.txt
# same path / olivia.txt
