import re

# .sub()
# substitute
# takes three arguments
# 1 regex pattern
# 2 replacement string
# 3 string to search & replace

email_text = "Contact us at info@example.com or support@mywebsite.com."
regex = r"\w+@" # the username portion of the email address
anonymised = re.sub(regex, "user@", email_text)
print(anonymised) # Contact us at user@example.com or user@mywebsite.com.

# BACK REFERENCING
# a way to refer back to matched groups in the pattern

month_text = "The event will take place on the 02/14/2024. Please purchase tickets by 01/01/2024."
pattern = r"(\d{2})/(\d{2})/(\d{4})"
reformat_dates = re.sub(pattern, r"\3-\1-\2", month_text)
print(reformat_dates)
# The event will take place on the 2024-02-14. Please purchase tickets by 2024-01-01.