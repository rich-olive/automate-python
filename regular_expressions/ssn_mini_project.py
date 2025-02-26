import re
# create a function to mask digits of a social security number
# normal format of SSN: 3 digits-2 digits-4 digits
# example: 321-54-9876
# we want to out put ***-**-9876
# if an incomplete number in inputted, we shouldn't do anything with it
# maybe an error message?

def anonymise_ssn(ssn: str):
    regex_valid_ssn = r"(\d{3})-(\d{2})-(\d{4})"
    regex_false_ssn = r"(\d{3})-(\d{2})$"
    anonymised_regex = r"(\d{3})-(\d{2})"
    modified_ssn = ""
    # validate snn length
    if re.match(regex_false_ssn, ssn):
        print(ssn)
    elif re.match(regex_valid_ssn, ssn):
        modified_ssn = re.sub(anonymised_regex, "***-**", ssn)
        print(modified_ssn)
    else:
        print("Invalid social security number")
    # validate snn contains only digits and hyphens in format 000-00-0000
    # .match to validate
    # .group to isolate groups (000)-(00)-(0000)
    # .sub to replace the numbers with ***

# anonymise_ssn("321-54-9876") # valid
# anonymise_ssn("321-54-876") # invalid, too few digits
# anonymise_ssn("321-549876") # invalid, missing hyphen
# anonymise_ssn("321/54-9876") # invalid, slash instead of hyphen
# anonymise_ssn("3a1-54-9876") # invalid, letter instead of number
# anonymise_ssn("321-54") # invalid, too few digits -> this is a separate case


# SOLUTION

def mask_ssn(text):
    regex = regex_valid_ssn = r"\d{3}-\d{2}-(\d{4})"
    # creates only one group in the regex string: (\d{4})
    clean_ssns = re.sub(regex, r"***-**-\1", text)
    # back referencing in the replace string: \1 - targets that one and only group
    return clean_ssns

sample_text = "An example of a valid SSN is 321-54-9876. However, 321-45 is NOT a valid SSN."
print(mask_ssn(sample_text)) # An example of a valid SSN is ***-**-9876. However, 321-45 is NOT a valid SSN.
