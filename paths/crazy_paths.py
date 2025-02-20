from pathlib import Path

crazy_path = Path.home() / "I" / "dont" / "exist.csv"

print(crazy_path)
# C:\Users\olivi\I\dont\exist.csv
# it looks like this file and path actually exist

with open(crazy_path, "r") as file:
    print(file.read())
# but when we try to open it:
# FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\olivi\\I\\dont\\exist.csv'