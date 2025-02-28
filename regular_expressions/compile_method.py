import re
# COMPILE METHOD
# compiles a regex pattern into a regex object
# the object stores the pattern
# can be used to call findall or search, etc
# makes performance better
# good if re-using the same regex pattern several times

content = 'test'

phone_regex = re.compile(r"\(?\d{3}\)?[- ]\d{3}[- ]\d{4}")
email_regex = re.compile(r"([\w\.]+@\w+\.(com|org|net|co.uk))", re.IGNORECASE)
# compile method takes a second argument for compilation flags

phone_matches = re.findall(phone_regex, content)
# can use findall, group, search, etc as normal on the regex object!