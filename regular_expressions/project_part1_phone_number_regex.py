import re

# define regex patterns

# phone number
# ex 1 123-456-7890
# ex 2 123 456 7890
# ex 3 (123)-456-7890

phone_number_regex = r"((\(\d{3}\)|\d{3})(-|\s)\d{3}(-|\s)\d{4})"
# email
# website
# read example email file

# save the values
# add to a new .txt file

# sample numbers
test_number_hyphen = "404-599-6732"
test_number_space = "203 543 2178"
test_number_bracket_hyphen = "(606)-456-7890"
test_number_bracket_space = "(606) 126 8547"

# checking samples against regex
check_number_hyphen = re.search(phone_number_regex, test_number_hyphen)
check_number_space = re.search(phone_number_regex, test_number_space)
check_number_bracket_hyphen = re.search(phone_number_regex, test_number_bracket_hyphen)
check_number_bracket_space = re.search(phone_number_regex, test_number_bracket_space)

# display results
if check_number_hyphen is not None:
    print(check_number_hyphen.group())
else:
    print("invalid")

if check_number_space is not None:
    print(check_number_space.group())
else:
    print("invalid")

if check_number_bracket_hyphen is not None:
    print(check_number_bracket_hyphen.group())
else:
    print("invalid")

if check_number_bracket_space is not None:
    print(check_number_bracket_space.group())
else:
    print("invalid")
