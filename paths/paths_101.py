from pathlib import Path

p = Path(".")

print(f"\n{p} is the current working directory")

home = Path.home()
print("The home directory is ", home)
# The home directory is  C:\Users\olivi

doc_path = home / 'documents'
# add 'documents' to home path
# C:\Users\olivi\documents

print(doc_path)

file_path = doc_path / 'my_file.txt'
# do a similar thing for the file

print(file_path)
# C:\Users\olivi\documents\my_file.txt

with open(file_path, "r") as file:
    print(file.read())
# then use the predefined home, doc path & file path to locate and open the txt file.

print(doc_path.parent)
# C:\Users\olivi