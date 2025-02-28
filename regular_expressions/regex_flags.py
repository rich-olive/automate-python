import re
# COMPILATION FLAGS
# IGNORECASE FLAG
# ignores the case to return all instances of the searched-for text
# third argument in .findall()
text = "Python is fun, but PYTHONS are scary!"

matches = re.findall('Python', text, re.IGNORECASE)

print(matches)

# MULTILINE FLAG
bad_poem = '''
Python, in your syntax we find delight,
Turning complex problems into something light,
python, your eloquence is truly a sight,
In the world of coding, you are a knight. 
'''

# the first character of this string is technically a newline character
# even moving it up, the .findall() only returns 'Python' and not 'python' because
# of the multi line nature of the text

poem_matches = re.findall("^python", bad_poem, re.IGNORECASE | re.MULTILINE)
# use | to chain multiple flags
print(poem_matches)

# DOTALL FLAG
# the dot looks for every character except the newline character
# this flag includes the newline in the dot

dot_matches = re.findall("light.+python", bad_poem, re.IGNORECASE | re.DOTALL)
print(dot_matches)