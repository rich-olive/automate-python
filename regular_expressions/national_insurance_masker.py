import re

valid_nin_regex = r"([A-Z]{2}[0-9]{2})([0-9]{4})([A, B, C, D]{1})"

def anonymise_nin(nin):
    validate_input = re.search(valid_nin_regex, nin)
    part_to_modify = validate_input.group(2)
    if validate_input is not None:
        modified_nin = re.sub(part_to_modify, "****", nin)
        print("Your National Insurance number is:\n",modified_nin)
    else:
        print("Invalid National Insurance number")


while True:
    nin_input = input("Please enter your National Insurance number:\n")

    if re.search(valid_nin_regex, nin_input.upper()) is None:
        print("Invalid National Insurance number.\n")
    else:
        anonymise_nin(nin_input.upper())
        break

