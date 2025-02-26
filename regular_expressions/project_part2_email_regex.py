import re

email_regex = r"(\w+@\w+\.(com|co.uk|org|net))"

test_email_com = "myname@website.com"
test_email_co_uk = "olivia@organisation.co.uk"
test_email_org = "support@tech.org"
test_email_net = "hello@oursite.net"
test_email_bad_email = "@gmail.com"
test_email_bad_email2 = "hi@office.co"
test_string_containing_email = "you can contact our office at support@office.com"

check_email_com = re.search(email_regex, test_email_com)
check_email_co_uk = re.search(email_regex, test_email_co_uk)
check_email_org = re.search(email_regex, test_email_org)
check_email_net = re.search(email_regex, test_email_net)
check_email_bad_email = re.search(email_regex, test_email_bad_email)
check_email_bad_email2 = re.search(email_regex, test_email_bad_email2)
check_string_containing_email = re.search(email_regex, test_string_containing_email)

if check_email_com is not None:
    print(check_email_com.group())
else:
    print("invalid")
if check_email_co_uk is not None:
    print(check_email_co_uk.group())
else:
    print("invalid")
if check_email_org is not None:
    print(check_email_org.group())
else:
    print("invalid")
if check_email_net is not None:
    print(check_email_net.group())
else:
    print("invalid")
if check_email_bad_email is not None:
    print(check_email_bad_email.group())
else:
    print("invalid")
if check_email_bad_email2 is not None:
    print(check_email_bad_email2.group())
else:
    print("invalid")
if check_string_containing_email is not None:
    print(check_string_containing_email.group())
else:
    print("invalid")