import re

phone_regex = r"\(?\d{3}\)?[- ]\d{3}[- ]\d{4}"

# ? to make the () optional
# \ to escape the ()
# [] to match any one of a series of characters

email_regex = r"([\w\.]+@\w+\.(com|org|net|co.uk))"
# [] series -> because often emails are firstname.surname
# \ to escape the .
# followed by + -> accounts for several characters
# () to enclose a group (com, org, etc)
# | to look for any of them
# .findall() only returns matches to groups if we use groups in our regex
# so we need to wrap the whole string in ()

web_regex = r"(^|\s)(\w+\.(com|org|net|co.uk))"
# (^|\s) to capture a start of string or whitespace character (no @ preceding)
# (\w+\.(com|org|net|co.uk) literally copied and pasted the latter half of the email regex
# added () round the domain name part so we can isolate from the initial whitespace

with open("example_email.txt", "r") as file:
    content = file.read()

phone_matches = re.findall(phone_regex, content)
email_matches = re.findall(email_regex, content, re.IGNORECASE)
website_matches = re.findall(web_regex, content, re.IGNORECASE)

phone_list = []
for phone in phone_matches:
    line = phone + "\n"
    if line not in phone_list:
        phone_list.append(line)

with open("phone_nums.txt", "w") as file:
    file.writelines(phone_list)

email_list = []
for email in email_matches:
    line = email[0] + "\n" # to isolate the actual email
    if line not in email_list:
        email_list.append(line)

with open("email_adds.txt", "w") as file:
    file.writelines(email_list)

# using findall method with a regex expression that contains groups, it produces a tuple, not a list
# so we use email[0] to index the tuple and get the whole string, rather than ['example@gmail.com', 'com']

print(website_matches) # [('', 'TechFusion.com', 'com'), (' ', 'TechSupport.net', 'net'),
# (' ', 'PMguidelines.org', 'org'), (' ', 'TechFusion.com', 'com')]
# each match is a tuple, the first element of which is the white space, the second is the actual website and the
# third is the .com/.org etc

website_list = []
for website in website_matches:
    line = website[1] + "\n" # to isolate the actual website
    if line not in website_list:
        website_list.append(line)
print(website_list) # ['TechFusion.com\n', 'TechSupport.net\n', 'PMguidelines.org\n']
# so that explains the use of () to group regex: the findall method returns a tuple
# which needs indexing to work with!

with open("website_adds.txt", "w") as file:
    file.writelines(website_list)
