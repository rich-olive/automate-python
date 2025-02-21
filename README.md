# Automate Python Course
This repository documents my progress through **The Python Automation Bootcamp (Work Smarter!): Zero to Mastery** [https://zerotomastery.io/courses/learn-python-automation/].
The course is broken up into sections: 

* Working with Files
* Paths and Folders
* Regular Expressions
* Automating Spreadsheets
* Automating Email
* APIs
* Automating ChatGPT

I have created separate branches for each section, and then merged them into main once complete. 

## Product Sales Tracker
The first project was a product sales tracker, in which some basic data (product codes) was provided in .txt format for me to convert into a meaningful spreadsheet. Using the raw data, I mapped product codes to product names and unit prices stored in a dictionary. I used enumerate() in a for loop to add a sequence of sale (this item was purchased first, that item second, etc.). I used datetime.date.today() and % format specifiers to add a correctly-formatted current date to each row. Finally, this more meaningful data was outputted as a spreadsheet (.csv) file. 

I ran into a couple of issues when building this programme, namely I accidentally converted a dictionary look-up into a tuple, so the output was incorrect: asking ChatGPT a few questions (it alerted me to the fact that Python will identify a trailing comma as a tuple) and combing through the code helped me to catch the error. Also, the current date was misformatted in the spreadsheet; I researched format specifiers to fix this. 

As I wrote *a lot* of comments to help me pseudo code, think through issues, and recall output, I subsequently created a refactored project file without the comments, and with some small bits of refactoring to make the code cleaner and easier to read. I have kept the original project file as documentation, and so I can review my thinking and solutions. 

This first project has also helped me to get back into the flow of using git commands. Even writing this README has improved my knowledge of markdown. It's been a very positive and fruitful project for me!

This project inspired me to create the Shopping List applet. This applet runs as a CLI in which users can select user-defined number of meals from a list, and a shopping list of ingredients and quanitites is created in spreadsheet format. 
