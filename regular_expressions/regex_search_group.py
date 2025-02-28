import re


# search method - does a pattern exist in a string
# takes two args, pattern to match, string to search
# if it finds it, returns match object
# otherwise it returns none

joke = "I remixed a remix, it was back to normal"
match = re.search("remix", joke)
# search method returns the first match it finds!

if match is not None:
    print("We found a match")
else:
    print("No match was found")

# the group method shows us the actual matched string

print("The match is", match.group())

codes = '123abc xyz789 gh12ij'
pattern = r'\d\w+'
code_match = re.search(pattern, codes)

print("the match is", code_match.group())


test_string = "the parcel will arrive on June 21, 2023"
regex = r"(\w+) (\d{1,2}), (\d{4})"
# alphanumerics 1 or more
# space
# digits, one or two for the date
# comma, space
# 4 digits for year

# brackets used to group the individual bits of data
# the brackets don't have an effect on the regex

regex_no_comma = r"(\w+) (\d{1,2}) (\d{4})"

match_test_string = re.search(regex, test_string)
# print(match_test_string.group())

# we can pass an integer as an argument to .group() to return the separate
# pieces of data: [1] "June", [2] "21", [3] "2023"

# can chain .search() and .group() together

# print(match_test_string.group(1)) # June
# print(match_test_string.group(2)) # 21
# print(match_test_string.group(3)) # 2023


user_birthday_input = input("Please enter your birthday month/dd/yyyy:\n")
check = re.search(regex_no_comma, user_birthday_input)

if check is not None:
    print("You were born in", check.group(1))
else:
    print("Invalid date format")
