with open("poem.txt", "w") as file:
   file.write("Roses are red,\n")
   file.write("Violets are blue.\n")
   file.write("Sugar is sweet,\n")
   file.write("And so are you!\n")

with open("poem.txt", "r") as file:
   print(file.read())

# behaviour with "w" mode is to overwrite the data every time
# must use "a" (append) to append data