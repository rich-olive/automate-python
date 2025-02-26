# patterns used for text processing
# describe patterns of text using sequence of characters
# work across many languages

# literals and metacharacters
# literals are the literal characters
# metacharacters stand in for something else

# data validation - passwords, emails
# data extraction from large text files

# sometimes it is better to use a simpler method

# regex are case sensitive
# the dot . is a wildcard
# .at
# will find cat, rat, bat and hats
# so not just limited to 3 letter words

# use \ to escape . if we want to find .

# \d any digit 0-9
# \D any non digit character
# \w any alphanumeric character (a-z, A-Z, 0-9)
# \W any non-alphanumeric character (spaces, commas, etc)
# \s any whitespace
# \S anything that isn't whitespace

# CHARACTER RANGE
# character range using brackets
# [0-9] will match any numbers
# and can use with letters [a-z]
# [a-zA-Z] identifies any letters
# [0-9A-Za-z] identifies numbers or letters

# can use to match random stuff like t l c 1 4 9
# [tlc149]
# [tlc1-3]
# [0-9][a-z] finds any instance of a lower case letter following a number
# [yV4-9]
# [^a-zA-Z0-9] anything but these alphanumerics

# QUANTIFIERS
# * + ?
# * = matches zero or more instances of previous character
# pythonnnnn | Python* = this matches because the n can occur many times
# + = prev characters 1 or more
# ? = zero or once, optional

# \d+!*
# this requires one or more ! after a digit/s

# CUSTOM QUANTIFIERS
# a{2} = matches 'aa'
# a{3,6} = matches 'aaa','aaaa','aaaaa','aaaaaa'
# a{6,} = matches everything from 'aaaaaa'
# \d{3}-\d{3}-\d{4}
# Is 859-867-5309 a real number?

# ANCHORS
# where in a string our pattern should match
# ^ denotes start of the string
# $ denotes end of string
# ^Hello = only matches start of string hello
# ^\d{5}$ = only looking for a 5 digit number with nothing preceding or following

# IGNORECASE
# ignores the case

# MULTILINE
# makes ^ and $ match entire lines, instead of entire string

# DOTALL
# makes the dot character match all characters, including new lines

