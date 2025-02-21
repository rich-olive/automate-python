# Quick deep dive into dictionaries
# From 'Python Crash Course' by Eric Matthes

# dictionaries allow us to connect pieces of related information
# dicts allow us to model a variety of real-world objects
# e.g. people: name, age, profession
# can store any 2 kinds of info that can be matched up
# e.g. list of words and their meanings (much like an actual dictionary!)

# seems like they are basically like JavaScript objects
alien = {"colour": "green", "eyes": 4}
# curly brackets
# key-value

print(alien["colour"])
# access using square brackets and name of key

# use the key to access the value
# a key's value can be a number, string, list or another dictionary: any object

# retrieving and using a value
print(f"The alien has {alien["eyes"]} eyes!!")
if alien["eyes"] > 2:
    print("OMG, so many eyes!!")

count = 0
while count < alien["eyes"]:
    print("Hi, ️👽👁️")
    count += 1

# dicts are dynamic: we can add new key-values at any time
print(alien)
alien["legs"] = 13
alien["home planet"] = "Mars"
print(alien)

# from python 3.7, dictionary values retain order in which they were added

# can instantiate an empty dictionary
cars = {}

# can modify values in a dict
alien["colour"] = "red"
print(alien)

# to permanently delete a key-value pair
del alien["legs"]
print(alien)

# so far the examples have pertained to different info about one object
# we can also list info for multiple objects
# e.g. listing fave programming languages for different people

location_specific_snacks = {
    "cinema": "popcorn",
    "beach": "corn on the cob",
    "sports event": "hotdog",
    "birthday party": "cake",
    "winter walk": "hot chocolate"
}

print(f"When I'm at the cinema, I like to have {location_specific_snacks["cinema"]}.")
print(f"When I'm at the beach, I like to have {location_specific_snacks["beach"]}.")
print(f"When I'm on a winter walk, I like to have {location_specific_snacks["winter walk"]}.")

# if trying to access a key that doesn't exist: Traceback/ KeyError
# can handle using .get()

theme_park_snack = location_specific_snacks.get("theme park", "No snack value assigned")
print(theme_park_snack)

# exercises
# model a person
olivia = {
    "name": "Olivia",
    "age": 32,
    "city": "London"
}

print(olivia["name"])
print(olivia["age"])
print(olivia["city"])

# add favourite numbers for five people
fave_numbers = {
    "raphael": 3,
    "hillel": 6,
    "babak": 13,
    "anushiravan": 28,
    "wesam": 44
}

print(f"Raphael's favourite number is {fave_numbers["raphael"]}")
print(f"Hillel's favourite number is {fave_numbers["hillel"]}")
print(f"Babak's favourite number is {fave_numbers["babak"]}")
print(f"Anushiravan's favourite number is {fave_numbers["anushiravan"]}")
print(f"Wesam's favourite number is {fave_numbers["wesam"]}")

# model a glossary of five key programming terms

# from automate python section on python

translations = {
    "hello" : "salam",
    "goodbye" : "khodahafez",
    "yes" : "baleh"
}

# length of a dictionary
print(len(translations))

# benefits of using a dictionary over a list
# example: a list of students and their grades

students_list = [
    ["Olivia", 32, [85, 90, 95]],
    ["Guy", 29, [82, 92, 90]],
    ["Lisa", 66, [96, 99, 100]]
]

# using a list, each student is a nested list containing name, age and another nested list
# containing their grades from 3 classes
# thus trying to access specific data from this list is tricky
# how to access Lisa's second grade?
# we'd need to know that Lisa is the third nested list, etc.

students_dictionary = {
    "Olivia": {"age": 32, "grades": [85, 90, 95]},
    "Guy": {"age" : 29, "grades" : [82, 92, 90]},
    "Lisa": {"age" : 66, "grades" : [96, 99, 100]},
}

# using a dictionary, it's much easier to access the info we need
# now we can look up Guy's grades by targeting students_dictionary["Guy"]

olivia_age_from_list = students_list[0][1]
print(f"Olivia's age from a list: {olivia_age_from_list}")
olivia_age = students_dictionary["Olivia"]["age"]
print(f"Olivia's age is {olivia_age}.")

# less traversal as well!

lisa_grade_2 = students_dictionary["Lisa"]["grades"][1]
print(f"Lisa's second grade: {lisa_grade_2}")

# looping over a dictionary
# each iteration of looping over a dictionary can give us a key, a value or both

person = {
    "name": "Olivia",
    "age": 32,
    "job": "office pig"
}

# loop/print each key
for key in person:
    print(key)

# .values() to print the values
print(person.values())
# dict_values(['Olivia', 32, 'office pig'])
for value in person.values():
    print(value)

# access keys and values
# generate readable summaries

# .items()
print(person.items())
# dict_items([('name', 'Olivia'), ('age', 32), ('job', 'office pig')])
# list of tuples

# tuple unpacking
# each item returned by .items() is a tuple containing 2 items (key and its value)
# we can unpack those two into separate variables

for key, value in person.items():
    output = f"{key} : {value}"
    print(output)