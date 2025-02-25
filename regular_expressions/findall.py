import re
# findall similar to .search
# finds all instances of the pattern
# takes 2 args: pattern to match & string to check
# it does not return a match object
# it returns a list of matching strings

regex = r"\d{4}"
# best practice to convert regex string to raw string!!
test_string = ("The World Cup of 1998 was held in France. The next event in 2002 was held in South Korea. "
               "The most recent World Cup was held in Qatar in 2022.")

world_cup_years = re.findall(regex, test_string)
# .findall() is a method on re object/package

print(world_cup_years) # ['1998', '2002', '2022']
# list of strings
# the order determined by the order they appeared in the string

cat_regex = r"meo+w+"
cat_text = "The cat goes meow, meooooow, meooow, meowwwww, whilst the dog goes woof."
sounds = re.findall(cat_regex, cat_text)
print(sounds) # ['meow', 'meooooow', 'meooow', 'meowwwww']