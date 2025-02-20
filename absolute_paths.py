# the dad_jokes.txt is no longer in the project folder, now saved to absolute_v_relative folder
# from the address bar, right click and select copy address as text
# C:\Users\olivi\PycharmProjects\automate_python\absolute_v_relative

path = "C:\\Users\olivi\PycharmProjects\\automate_python\\absolute_v_relative\dad_jokes.txt"

# beware escape characters
# add the actual file name at the end: dad_jokes.txt

# previously just passed in the file name
# that was an implicit file path
with open(path, "r") as file:
    print(file.read())

