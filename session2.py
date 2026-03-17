print("Hello", "World!")

# Syntax is clean and readable
x = 5
if x < 10:
    print("x is less than 10")
else:
    print("x is 10 or more")
    
    
# Local vs Global Variables
# def func():
#     name = “Alice”
#     age = 45


# local variable example
def my_function():
    x = 10 # x is a local variable
    print(x)
    
checker = 10
checker = 2 # overwritten value so it will be 2
print(checker)
# my_function(x)


# global variable example
x = 10 # x is a global variable
def my_function():
    global x # declare x as a global variable within the function
    x += 5
    print(x)
my_function()


# string concatenation
string1 = "Programming"
string2 = "class"
result = string1 + " " + string2 #concatenation
print(result)


# string slicing
message = "Hello World"
text = message[0:5] # slicing (from index 0 to 5)
print(text) 


# string formatting
name = "ABC"
age = 30
fstring= f"My name is {name} and I am {age} years old." # string formatting
print(fstring) 