import re


# REGEX PATTERNS
phone_number_regex = r"((\(\d{3}\)|\d{3})(-|\s)\d{3}(-|\s)\d{4})"
email_regex = r"(\w+@\w+\.(com|co.uk|org|net))"
website_regex = r"((^|\s|)(\w+\.(com|org|net|co\.uk)))"

email_addresses = []
websites = []

# READ TEXT FILE
with open("example_email.txt", "r") as file:
    text = file.read()
# PARSE TEXT FOR PHONE NUMBERS
check_phone_numbers_in_text = re.findall(phone_number_regex, text, re.IGNORECASE | re.MULTILINE)
list_of_phone_numbers = [number[0] for number in check_phone_numbers_in_text]
remove_duplicate_phone_numbers_list = list(dict.fromkeys(list_of_phone_numbers))

# PARSE TEXT FOR EMAILS

# PARSE TEXT FOR WEBSITES

# WRITE PHONE NUMBERS TO NEW FILE
with open("phone_numbers.txt", "w") as phone_numbers_file:
    for item in remove_duplicate_phone_numbers_list:
        phone_numbers_file.write(item + "\n")

# WRITE EMAILS TO NEW FILE
# WRITE WEBSITES TO NEW FILE