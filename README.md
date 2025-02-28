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

## Clean Sweeper 
After learning about paths and about copying, moving, iterating over, renaming and deleting files and folders, I put my new skills to use to complete the Clean Sweeper project. In the course resources is a messy folder containing different types of files (.txt, .csv, .xslx, .pptx, .docx) and variously named sub folders.

The task was to create a new folder ("closet") and three sub folders, and then to iterate over the messy folder, sorting each file or folder into one of the newly-created folders depending on certain stipulations (e.g. any folder containing the word "temp" in its name was to be deleted, any file of type .txt was to be moved to the text_files sub folder).

It was a bit tricky getting my head around the different file paths to begin with. I now have a better understanding of several methods included in the PathLib and Shutil modules. An interesting takeaway from this project is the concept of a "raw string" (raw strings ignore escape character sequences, according to realpython.com), and the fact that the input() function automatically converts user-defined input into a raw string.

Unlike the previous project, in which I documented all my attempts and their outputs, in this project, after writing out the requirements in comment form, I quickly made the decision to create a new project file (refactored_clean_sweeper_project) and to keep it as clean and clear as possible. This really helped me keep a clear head when dealing with the many different paths.

After solving the project independently, I watched the solution video. I then copied out the solution code and analysed each line. It was much cleaner than my own code, and it also highlighted some points that I missed or forgot from the previous lessons. 

Overall, it was fun watching the files be effortlessly sorted into the correct folders, and I am pleased with the neat little script I wrote!

## Contact Info Extractor Project

This whole section has finally helped me to understand regular expressions after years of avoiding the topic! I feel a lot more confident to tackle problems using regex now. 

In this project, an example text file was provided. It contained an email message concerning a business transaction. In it were several phone numbers, email addresses and website addresses. The goal was to write a program, using regex, to parse this email and extract all the phone numbers, email addresses and website addresses, and then create a new text file for each. 

The hardest part of the project was writing the regex patterns. I decided to write and test each pattern in separate files, hence there is "project_part1_phone_number_regex.py", etc. I tried to test for different cases, such as phone numbers with hyphens or spaces, invalid email addresses, and whether a string contained an email address or a website. After practising and testing the patterns, I moved onto writing the logic for the actual program. The patterns needed tweaking as I worked. The reading and writing of new files felt quite comfortable (though I did forget about the .writelines() method!). 

I was pleased with how quickly the project came together, and I actually had a lot of fun writing the test cases. I couldn't get my head around how to strip out the whitespace from the start of website addresses. I went a bit overkill on trying to remove duplicate values by writing a function and then using that function in a for loop; this was mostly to test whether it would work, however, which I figured it would due to the first class citizenship of functions in Python. 

After finishing the project, I watched the solution videos and typed out the code with comments to understand exactly what was going on. I found it really helpful to do this! It helped me better understand some key regex features such as character ranges and using the optional metacharacter (?). Crucially, it enabled me to understand where I had gone wrong with not being able to strip the whitespace from the website addresses!

The .findall() method, when used with a regex pattern containing a group (indicated by the use of brackets()), returns a list containing tuples. So, the results for websites looked like this:

```[('', 'TechFusion.com', 'com'), (' ', 'TechSupport.net', 'net'), (' ', 'PMguidelines.org', 'org'), (' ', 'TechFusion.com', 'com')]```

In order to remove the whitespace, we have to index the tuple using square bracket notation, to ensure we target the actual domain name part of the result (e.g. "TechFusion.com"), rather than just adding the entire tuple to the new text file. I now better understand the use of brackets to create groups in regex patterns. 

It was a great project, overall!

