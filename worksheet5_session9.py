# # 1.2 Exercise 1
# '''
# 1.2 Exercise 1
# You are practising Python error handling and file operations. The task is to create a text file containing
# a few lines summarising what you have learned about Python. After creating the file, the program
# should read its contents in two ways:
# a) Reading the entire file content at once and printing it.
# b) Now read the file line by line into a list and printing each line in a loop.
# Additionally, we need to implement error handling to ensure that the program can gracefully handle
# issues like missing files or permission errors. Using OOP, the solution will encapsulate the logic within
# a class.
# You can also use the students.csv file to complete parts a and b.
# '''
# class PythonLearningFile:
#     def __init__(self, filename):
#         self.filename = filename
#     # create and write to the file
#     def create_file(self):
#         try:
#             with open(self.filename, "w") as file:
#                 file.write("I learned Python in college\n")
#                 file.write("It was fun and easy to understand\n")
#                 file.write("I really enjoy it\n")
                
#                 print("File created successfully\n")
#         except PermissionError:
#             print("Permission denied: Cannot write to the file")
#         except Exception as e:
#             print(f"An error occured: {e}")
            
#     # part A. read entire file at once
#     def read_all_content(self):
#         try:
#             with open(self.filename, "r") as file:
#                 content = file.read()
#             print("=== Reading Entire File ===")
#             print(content)
#         except FileNotFoundError:
#             print("Error: File not found")
#         except PermissionError:
#             print("Permission denied: Cannot read the file")
#         except Exception as e:
#             print(f"An error occured: {e}")
            
#     # part B. read file line by line into a list
#     def read_line_by_line(self):
#         try:
#             with open(self.filename, "r") as file:
#                 lines = file.readlines()
#             print("==== Reading file line by line ====")
#             for line in lines:
#                 print(line.strip())
#         except FileNotFoundError:
#             print("Error: File not found")
#         except PermissionError:
#             print("Permission denied: Cannot read the file")
#         except Exception as e:
#             print(f"An error occured: {e}")

# # create object
# my_file = PythonLearningFile("python_learning.txt")

# # create the file
# my_file.create_file()

# # part A
# my_file.read_all_content()

# # part B
# my_file.read_line_by_line()


# # 1.3 Exercise 2
# '''
# Read each line from a file named learning_students.txt and replace any words that are learner with
# the word student. Then, print the modified lines to the screen.
# a) Create the Input File (learning_students.txt)
# 1. First, create a text file named learning_students.txt and add some content that includes
# the word learner.
# 2. Example of content for the file learning_students.txt.
# Every learner must complete their assignments on time. A good learner always seeks to learn
# more. Learners are the future leaders.
# b) Write Python Code to replace learner with student.
# 1. You will use Python to read the file line-by-line, replace occurrences of learner with
# student, and print the modified lines.
# '''
# class FileModifier:
#     def __init__(self, filename):
#         self.filename = filename
    
#     # create the input file
#     def create_file(self):
#         try:
#             with open(self.filename, "w") as file:
#                 file.write("Every learner must complete their assessments on time\n")
#                 file.write("A good learner always seeks to learn more\n")
#                 file.write("Learners are the future leaders\n")
#             print("File created succesfully\n")
#         except Exception as e:
#             print(f"An error occured while creating the file: {e}")
            
#     # read file and replace words
#     def replace_words(self):
#         try:
#             with open(self.filename, "r") as file:
#                 lines = file.readlines()
#             print("=== Modified Lines ===")
#             for line in lines:
#                 modified_line = line.replace("learner", "student")
#                 modified_line = modified_line.replace("Learners", "Students")
#                 print(modified_line.strip())
#         except FileNotFoundError:
#             print("Error: File not found")
#         except PermissionError:
#             print("Permission denied: Cannot access the file")
#         except Exception as e:
#             print(f"An error occured: {e}")
            
# # create object
# my_file = FileModifier("learning_students.txt")

# # create file
# my_file.create_file()

# # replace and print modified text
# my_file.replace_words()


# # 1.4 Exercise 3
# '''
# One common issue encountered when asked to enter numerical input is accidentally entering alpha
# instead of numeric. When trying to convert an input value to an int, this will trigger a ValueError.
# a) Write a program that prompts (stdin) the user to enter two numeric values.
# 1. Add the two numeric values together and display the result.
# 2. Test 1. Print to stdout by entering two valid numerics to test whether the code block
# works.
# b) If an alpha character is entered instead of a numeric value, catch the ValueError and display
# a friendly error message reminding them to enter numbers only.
# 1. Test 2. If the user enters an alpha character instead of a numeric value, the error
# message is displayed
# '''
# try:
#     num1 =int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
    
#     # add the numbers
#     total = num1 + num2
    
#     # display the result
#     print(f"The total is: {total}")
# except ValueError:
#     # error message if user enters text instead of numbers
#     print("Error: Please enter numbers only")


# # 1.5 Exercise 4
# '''
# Build a calculator that sends the total to stdout based on the entered numbers and is repeatable. If the
# user makes a mistake (e.g., entering an alpha character instead of a numeric one), the program will
# catch the error, display a helpful message, and continue running
# '''
# while True:
#     try:
#         # ask user for two numbers
#         num1 = float(input("Enter the first number: "))
#         num2 = float(input("Enter the second number: "))
        
#         # calculate total
#         total = num1 + num2
        
#         # display result
#         print(f"The total is: {total}")
#     except ValueError:
#         # handle invalid input
#         print("Error: Please enter numbers only")
        
#     # ask user if they want to continue
#     choice = input("Do you want to calculate again? (yes/no): ").lower()
    
#     if choice != "yes":
#         print("Calculator ended")
#         break


# # 1.6 Exercise 5
# '''
# This task involves working with a CSV file, students.csv, which contains students information, and
# splitting the student data into two files, students_c1.txt and students_c2.txt. The code will be
# wrapped in a try-except block to catch any FileNotFoundError and print a friendly message if a file
# is missing.
# a) Now, write a program to read the two files and print (stdout) their contents. Use a try-except
# block to handle any FileNotFoundError exceptions.
# b) Move one of the files (e.g., students_c1.txt) to a different folder on your system. Rerun the
# program and observe the output. It should display the friendly error message.
# c) Update the code to handle the missing file silently by writing an error log (error.log) to stderr
# in the except block. Move one of the files again (e.g., students_c2.txt). Run the program and
# confirm it does not raise an error or print any message if a file is missing, but has generated an
# error.log (or the file you have defined as the error message output file)
# '''
# # part A : Read the files with friendly error message
# files =["student_c1.txt", "student_c2.txt"]
# for filename in files:
#     try:
#         with open(filename, "r") as file:
#             print(f"\nContents of{filename}:")
#             print(file.read())
            
#     except FileNotFoundError:
#         print(f"Error: {filename} was not found")
        
# # part B - move one file and test
# # move one file such as "student_c1.txt"

# # part C - handle missing file silently and create error.log
# files = ["students_c1.txt", "student_c2.txt"]
# for filename in files:
#     try:
#         with open(filename, "r") as file:
#             print(f"\nContents of {filename}: ")
#             print(file.read())
#     except FileNotFoundError:
#         # write error message into error.log
#         with open("error.log", "a") as log_file:
#             log_file.write(f"Error: {filename} was not found\n")
#         # pass prevents program from crashing
#         pass


# # 1.7 Exercise 6
# '''
# Write a program to store the user’s favourite number.
# a) The program will prompt users to enter their favourite number and save it to a file using
# JSON.dumps().
# b) This program will read the favourite number from the file and display it in a personalised
# message.
# '''
# # store and read a favourite number using JSON
# import json
# filename = "favorite_number.json"

# # part A - ask user for favourite number and save it
# favorite_number = input("What is your favourite number?")
# with open(filename, "w") as file:
#     json.dump(favorite_number, file)
# print("Your favourite number has been saved\n")

# # part B - read the favourite number from the file
# with open(filename, "r") as file:
#     stored_number = json.load(file)
# print(f"I know your favourite number! it is {stored_number}")


# # 1.8 Exercise 7
# '''
# You will create a simple Python program that remembers a user’s favourite number. The program will
# check if a favourite number is stored in a file. If the number is stored, it will report it back to the user.
# If not, it will prompt the user to input their favourite number and store it in the file for future reference.
# We will combine all the necessary functions into a single program and run it twice to ensure it works
# correctly.
# a) Create a single Python code block that handles all the functionality needed to remember the
# user’s favourite number.
# b) The program will read from a file to determine if a favourite number is stored.
# c) If the favourite number is not found, the program will ask the user to enter and save their
# favourite number.
# d) Run the program two times to verify that the favourite number is correct.
# '''
# # remember user's favourite number
# import json
# filename = "favorite_number.json"
# try:
#     # try to read the favorite number from the file
#     with open(filename, "r") as file:
#         favorite_number = json.load(file)
#     print(f"I know your favourite number! it is {favorite_number}")
# except FileNotFoundError:
#     # ask the user for their favorite number
#     favorite_number = input("What is your favorite number?")
#     # save the number into the file
#     with open(filename, "w") as file:
#         json.dump(favorite_number, file)
#     print(f"We will remember your favorite number: {favorite_number}")


# #  1.9 Exercise 8
# '''
# You will create a simple Python program to collect user information and store it in a dictionary. You
# will be asked to create a file named user_profile.txt and populate it with IDs, such as student IDs. The
# second part of the program is to request two additional pieces of information. The program will
# serialise the dictionary to a JSON format, save it to a file, and then read it back, allowing us to retrieve
# and display the stored information. This process will demonstrate how to work effectively with
# dictionaries and JSON in Python.
# a) Collect user information and ask the user to enter and store the student ID. The data will be
# stored in a dictionary, then using the fuction JSON.dump()** to save to a file.
# b) Using the previously created file (a), load the file using JSON.load() and store the data into a
# dictionary.
# c) Using the data in the dictionary, ask the user to add two additional items for each students DOB
# and email address. Using the previously created file (a), write this additional data using
# JSON.dump() to the file.
# d) Create a summary report using data in the file created in (a) and print to stdout
# '''
# # student profile program using dictionary and JSON
# import json
# filename = "user_profile.txt"
# # part A - collect and store student ID
# student_profile = {}

# student_profile["student_id"] = input("Enter student ID: ")

# # save dictionary to file
# with open(filename, "w") as file:
#     json.dump(student_profile, file)
# print("student ID saved successfully\n")

# # part B - load data from file
# with open(filename, "r") as file:
#     student_profile = json.load(file)
# print("Loaded student data")
# print(student_profile)

# # part C - add DOB and email
# student_profile["dob"] = input("\nEnter data of birth: ")
# student_profile["email"] = input("Enter email address: ")

# # save updated dictionary back to file
# with open(filename, "w") as file:
#     json.dump(student_profile, file)
# print("\nAdditional information saved successfully")

# # part D - summary report
# with open(filename, "r") as file:
#     student_profile = json.load(file)
    
# print("\n=== Student Summary Report ===")
# print(f"Student ID: {student_profile["student_id"]}")
# print(f"Date of Birth: {student_profile["dob"]}")
# print(f"Email Address: {student_profile["email"]}")


# # 1.10 Exercise 9
# '''
# Create a code block in a file called remember_me.py. This program prompts the user for their name
# and store it in a JSON file. The goal is to ensure that the program can handle scenarios where the
# current user from the last user. The program will verify the user before storing their name.
# a) Create the necessary code to import the libraries for handling file paths and JSON data.
# b) Before prompting the user to save their name, check whether the username is already stored in
# a JSON file. If it exists, load the previous username.
# c) If the username exists (do not allow duplicate usernames), ask the current user whether it
# matches the previously stored user. If they are not, prompt for a new username.
# d) Regardless of whether the username is new or the same, store or overwrite the data in the JSON
# file.
# e) Print (stdout) a message confirming that the username has been saved or updated.
# '''
# # remember_me.py
# # program to store and verify username using JSON + file handling
# import json
# from pathlib import Path
# # file path
# filename = Path("remember_me.json")

# def load_username():
#     # load username if file exists
#     if filename.exists():
#         try:
#             with open(filename, "r") as file:
#                 data = json.load(file)
#                 return data.get("username")
#         except json.JSONDecodeError:
#             return None
#     return None

# def save_username(username):
#     # save username to JSON file
#     with open(filename, "w") as file:
#         json.dump({"username": username}, file)
        
# # load existing username (if any)
# stored_username = load_username()
# if stored_username:
#     print(f"Previously stored username: {stored_username}")
    
#     # ask if it matches current user
#     response = input("Is this you? (yes/no): ").lower()
    
#     if response != "yes":
#         username = input("Enter your new username: ")
#     else:
#         # no username stored yet
#         username = input("Enter your username: ")

# # save (overwrite or store new)
# save_username(username)

# print(f"Username '{username}' has been daved/updated successfully")