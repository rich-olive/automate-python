from pathlib import Path

# p = "C:\\Users\olivi\PycharmProjects\\automate_python\paths"

# we want to convert the text string into a path object
# convert to a raw string
# by adding 'r' before the string

p = r"C:\\Users\olivi\PycharmProjects\\automate_python\paths"
# works for mac and linux too (which use other slash)

# path = Path(p)
# Path here is a constructor
# we use it to create a path object

user_input = input("Enter a path:\n")
# input function automatically converts user input to a raw string

user_defined_path = Path(user_input)

if user_defined_path.exists():
    print("I exist")
else:
    print("I don't exist")

# C:\Users\olivi\PycharmProjects\automate_python\pat
# C:\Users\olivi\PycharmProjects\automate_python\paths

