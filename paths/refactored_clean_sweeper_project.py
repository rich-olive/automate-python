from pathlib import Path
import shutil

# PATH TO USE
# "C:\Users\olivi\Desktop\clean_sweep_project"

user_input = input("Enter a path:\n")
user_defined_path = Path(user_input)

closet_directory = user_defined_path / "closet"
text_files = closet_directory / "text_files"
csv_files = closet_directory / "csv_files"
folders = closet_directory / "folders"

if user_defined_path.exists():
    closet_directory.mkdir(exist_ok=True)
    text_files.mkdir(exist_ok=True)
    csv_files.mkdir(exist_ok=True)
    folders.mkdir(exist_ok=True)

    for item in user_defined_path.iterdir():
        src = user_defined_path / item.name
        if item.is_dir and "temp" in item.name:
            shutil.rmtree(item)
        elif item.is_dir() and not "closet" in item.name:
            src = user_defined_path / item.name
            dest = closet_directory / folders
            shutil.move(src, dest)
        elif item.is_file() and item.suffix == ".txt":
            dest = closet_directory / text_files
            shutil.move(src, dest)
        elif item.is_file and item.suffix == ".csv":
            dest = closet_directory / csv_files
            shutil.move(src, dest)
        elif item.is_file:
            dest = closet_directory
            shutil.move(src, dest)
    print("Clean up complete")
else:
    print("Folder does not exist")




