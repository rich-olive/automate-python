# file = open("test.txt", "r")
# content = file.read()
# print(content)
# file.close()


# this is a context manager; it manages opening and closing the file for us
with open("test.txt", "r") as file:
    lines = file.readline()

    for line in lines:
        print(line, end=" ")