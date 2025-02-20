from pathlib import Path

p = Path.home() / "documents" / "python_automation" /  "moving_and_renaming" / "my_fourth_folder" / "molivia.txt"
# only need to target the file, no source/dest required

p.unlink(missing_ok=True)
# this deletes the file
# missing_ok prevents an error when we have already deleted the file
# similar to checking for the existence of the file before running it
# part of pathlib

