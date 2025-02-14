additional_lines = ["Stars up above,\n", "Whisper words of love."]

with open("poem.txt", "a") as file:
    file.write("The sun is bright,\n")
    file.write("On this lovely night!\n")
    # add lines: it accepts an iterable as an argument
    # hence the list
    file.writelines(additional_lines[1])