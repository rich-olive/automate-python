import re

def remove_duplicates_from_list(list_of_data: list):
    return list(dict.fromkeys(list_of_data))

# REGEX PATTERNS
phone_number_regex = r"((\(\d{3}\)|\d{3})(-|\s)\d{3}(-|\s)\d{4})"
email_regex = r"(\w+@\w+\.(com|co.uk|org|net))"
website_regex = r"((^|\s)(\w+\.)(\w+))"

email_addresses = []
websites = []

# READ TEXT FILE
with open("example_email.txt", "r") as file:
    text = file.read()

# PARSE TEXT FOR PHONE NUMBERS
check_phone_numbers_in_text = re.findall(phone_number_regex, text, re.IGNORECASE | re.MULTILINE)
list_of_phone_numbers = [number[0] for number in check_phone_numbers_in_text]
# remove_duplicate_phone_numbers_list = list(dict.fromkeys(list_of_phone_numbers))

# PARSE TEXT FOR EMAILS
check_emails_in_text = re.findall(email_regex, text, re.IGNORECASE | re.MULTILINE)
list_of_emails = [email[0] for email in check_emails_in_text]
# remove_duplicate_email_addresses_list = list(dict.fromkeys(list_of_emails))

# PARSE TEXT FOR WEBSITES
check_websites_in_text = re.findall(website_regex, text, re.IGNORECASE | re.MULTILINE)
list_of_website_addresses = [website[0] for website in check_websites_in_text]

# remove_duplicate_website_addresses = list(dict.fromkeys(list_of_website_addresses))

# WRITE PHONE NUMBERS TO NEW FILE
with open("phone_numbers.txt", "w") as phone_numbers_file:
    for number in remove_duplicates_from_list(list_of_phone_numbers):
        phone_numbers_file.write(number + "\n")

# WRITE EMAILS TO NEW FILE
with open("email_addresses.txt", "w") as email_addresses_file:
    for email in remove_duplicates_from_list(list_of_emails):
        email_addresses_file.write(email + "\n")

# WRITE WEBSITES TO NEW FILE
with open("website_addresses.txt", "w") as website_addresses_file:
    for website in remove_duplicates_from_list(list_of_website_addresses):
        website_addresses_file.write(website + "\n")

# FINAL THOUGHTS
# the requirements mentioned a function to write lists of data to a text file in one fell swoop
# I couldn't think what it meant.
# I tried writerow and writerows, but the output was wrong,
# so I've stuck with a simple .write()

# I could not figure out how to remove the whitespace from the start of the website addresses

# the remove_duplicates function might be overkill, but mostly I wanted to see if you could use
# the result of a function in a for loop
# I figured yes because functions are first class citizens in python