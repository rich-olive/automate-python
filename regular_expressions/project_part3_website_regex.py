import re

# website regex
# need to distinguish from an email address
# not start with @
# whatever/however many characters

# This pattern should match website addresses
# that start with one or more alphanumeric characters,
# followed by a dot, and a domain ending in either "com", "net", or "org". >>> ".co.uk"

# sequence of alphanumeric characters, by requiring the preceding character to be either a whitespace character,
# or a start-of-string anchor.
# That way, you know for sure that the sequence of alphanumeric characters
# preceding the “dot” in the website address either comes at the beginning of the string,
# or after a word in the text -NOT after an “@” sign.

website_regex = r"((^|\s|www\.)\w+\.(com|org|net|co\.uk))"

# examples
test_website_com =  "website.com"
test_website_org = "yoursite.org"
test_website_net = "mysite.net"
test_website_co_uk = "oursite.co.uk"
test_website_www = "www.welcome.com"
test_email_or_website = "olivia@website.com"
test_string_containing_website = "you can visit our ourwebsite.com"


# function
check_website_com = re.search(website_regex, test_website_com)
check_website_org = re.search(website_regex, test_website_org)
check_website_net = re.search(website_regex, test_website_net)
check_website_co_uk = re.search(website_regex, test_website_co_uk)
check_website_www = re.search(website_regex, test_website_www)

check_email_or_website = re.search(website_regex, test_email_or_website)
check_string_containing_website = re.search(website_regex, test_string_containing_website)


if check_website_com is not None:
    print(check_website_com.group())
else:
    print("invalid")
if check_website_org is not None:
    print(check_website_org.group())
else:
    print("invalid")
if check_website_net is not None:
    print(check_website_net.group())
else:
    print("invalid")
if check_website_co_uk is not None:
    print(check_website_co_uk.group())
else:
    print("invalid")
if check_website_www is not None:
    print(check_website_www.group())
else:
    print("invalid")
if check_email_or_website is not None:
    print(check_email_or_website.group())
else:
    print("invalid") # prints "website.com"
if check_string_containing_website is not None:
    print(check_string_containing_website.group())
else:
    print("invalid")


# I'm not totally happy with how I've isolated web addresses from email addresses
# it could definitely use some work/more thought