# working with files - reading from a File
# created file contains pi to 30 decimal places, with 10 decimal places
# per line: pi_digits.txt (3.141592653589793238462643383279)
from pathlib import Path
path = Path("pi_digits.txt")
# read the entire contents of the file into a string
contents = path.read_text()
print(contents)


# rstrip() method
'''
Strip the trailing newline character when we read the contents of 
the file, by applying the strip() method immediately after calling 
read_text()
'''
from pathlib import Path
path = Path("pi_digits.txt")
contents = path.read_text()
contents = contents.rstrip()
print(contents)


# working with files - relative and absolute file paths
# relative file path
relative_path = Path("files/filename.txt")
# absolute file path
absolute_path = Path("C:\\Users\\data.txt\\files\\filename.txt")


# working with files - accessing a file's lines
# from pathlib import Path
# path = Path("greetings.txt")
# # read the entire contents of the file into a string
# contents = path.read_text()
# # split the string into a list of lines
# lines = contents.splitnes()
# # iterate through each line and print it
# for line in lines:
#     print(line)
    

# working with files - working with a file's contents
from pathlib import Path
path = Path("marks.txt")
numbers = path.read_text().splitlines()
total = 0
for num in numbers:
    num = int(num)
    # total = total + num
    total += num
print(total)


# working with files - large files: one million digits
from pathlib import Path
path = Path("pi_million_digits.txt")
# read the entire contents of the file into a string
contents = path.read_text()
# split the string into a list of lines
lines = contents.splitlines()
# initialise a variable to hold the digits of pi
pi_string = ""
for line in lines:
    pi_string += line.lstrip() #lstrip() removes any leading spaces
# print the first 50 decimal places and the length of the string 
print(f"{pi_string[:52]}...")
print(len(pi_string))


# working with files - writing to a file
from pathlib import Path
# create a path object representing the file "programming.txt"
path = Path("programming.txt")
# write a single line to the file
path.write_text("I love programming")


# working with files - writing multiple lines
from pathlib import Path
# define the contents of the file with multiple lines
contents = "I love programming\n"
contents += "I love creating new games\n"
contents += "I also love working with data\n"
# creating a path object representing the file
path = Path("programming.txt")
# writing the contents to the file
path.write_text(contents)


# exceptions - the ZeroDivisionError Exception
# attempting to divide by zeo raises a ZeroDivisionError print (5/0)
'''
ERROR!
Traceback (most recent call last):
    File "<main.py>", line 1, in <module>
ZeroDivisionError: division by zero
'''

# exceptions - using try-except blocks
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
    
    
# exceptions - the else block
print("Give me two numbers, and i will divide them")
print("Enter 'q' to quit")

while True:
    first_number = input("First number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    
    try: 
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)


# exceptions - analysing text
from pathlib import Path
path = Path("alice.txt")

try:
    contents = path.read_text()
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exists")
else:
    words = contents.split() # split(), splits the text into a list of words
    
    num_words = len(words) #len() function counts number counts number of words
    print(f"The file {path} has about {num_words} words")
    
    
# execptions - working with multiple files
from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words")
        
filenames = ["alice.txt" , "pi_digit.txt" "tittle_women.txt"]
for filename in filenames:
    path = Path(filename)
    count_words(path)
    

# exceptions - failing silently
def count_words(path):
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass #fail silently for missing files
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words")
        

# storing data - use json.dumps() and json.loads()
# json.dumps()
import json
from pathlib import Path

numbers = [2, 3, 5, 7, 11, 13]
path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)

# json.loads()
import json
from pathlib import Path

path = Path("numbers.json")
contents = path.read_path()
numbers = json.loads(contents)
print(numbers)
# numbers = [2, 3, 5, 7, 11, 13]


# storing data - saving and reading user-generated data
# json.dumps()
from pathlib import Path
import json

username = input("What is your name?")
path = Path("username.json")
contents = json.dumps(username)
path.write_text(contents)

# json.loads()
from pathlib import Path
import json

path = Path("username.json")
contents = path.read_text()
username = json.loads(contents)
print(f"Welcome back, {username}")


# storing data - combining programs (checking and handling existing data)
from pathlib import Path
import json

path = Path("username.json")

# check if the file exists
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}")
else:
    username = input("What is your name?")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}")
    
    
# refactoring - refacto greet_user()
from pathlib import Path 
import json

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
    else:
        return None
    
def get_new_username(path):
    username = input("What is your name?")
    conetnts = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path("username.json")
    username = get_stored_username(path)
    
    if username:
        print(f"Welcome back, {username}")
    else:
        username = get_new_username(path)
        print(f"We'll remember you whenn you come back, {username}")
        
greet_user()