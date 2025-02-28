# search for this OR that
# use | symbol
import re
from tokenize import cookie_re

sample = "the cat and the dog are friends"

regex = "cat|dog"

matches = re.findall(regex, sample)

print(matches) # ['cat', 'dog']
print(matches[1]) # dog


regex_two = r"(June|July) \d{1,2}"
# we must use brackets here to signify that June and July form a unit
# otherwise it would look for "June" or "July followed by 1-2 digits"
regex_three = r"((June|July) \d{1,2})"
# wrap the whole sentence in brackets as .findall() only matches in specific groups, not the whole sentence

sample_two = "I will be on holiday from June 21 to July 2."

matches_two = re.findall(regex_two, sample_two)
print(matches_two) # ['June', 'July']

matches_three = re.findall(regex_three, sample_two)
print(matches_three) # [('June 21', 'June'), ('July 2', 'July')]
# this is the one we wrapped entirely in brackets

fail_regex_dates = r"(\d{1,2}/\d{1,2}/\d{1,4}|\d{1,2}-\d{1,2}-\d{1,4})" # noooo

regex_dates = r"(\d{1,2}(-|/)\d{1,2}(-|/)\d{4})"
# using alternatio on -|/, wrap in brackets, wrap whole thing in brackets
# just use {4} to indicate 4 numbers instead of {1,4}
# {1,4} will actually allow incorrect date formats, such as '205', '3', '22', etc
# ['4/10/2024', '29-1-5']

dates_sample = "I think the date was 4/10/2024. Or it might've been 29-1-2025. Also, 7/05/2023, 12-8-2019 and 4/1"

date_matches = re.findall(regex_dates, dates_sample)
print(date_matches) # [('4/10/2024', '/', '/'), ('29-1-2025', '-', '-')]
# date_matches = re.findall(fail_regex_dates, dates_sample)
# print(date_matches)

print(date_matches[0][0], date_matches[1][0]) # 4/10/2024 29-1-2025
# the whole text is a group
# the smaller groups inside are sub groups
# returns a list of tuples
# with lots of data, could use a loop or list comprehension to extract

for item in date_matches:
    print(item[0])
    # 4/10/2024
    # 29-1-2025

list_of_dates = [item[0] for item in date_matches]
print(list_of_dates)
# ['4/10/2024', '29-1-2025']

