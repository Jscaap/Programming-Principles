# Worksheet 1, Session 2

# Variable Declaration and Types
# Declare two variables, a and b. Assign a the value 15 and b the value 12.
a = 15
b = 12
# Print the types of a and b using the type() function.
print(type(a)) # Output <class 'int'>
print(type(b)) # Output <class 'int'>


# Basic Arithmetic Operations
# Create a code script to perform an addition using (a + b) and print the result.
a = 5
b = 8
addition_result = a + b
print(addition_result) # Output 13

# Create a code script to perform a subtract (a - b) and print the result.
a = 10
b = 2
subtraction_result = a - b
print(subtraction_result) # Output 8

# Create a code script to multiply (a * b) and print the result.
a = 5
b = 5
multiply_result = a * b
print(multiply_result) # Output 25

# Create a code script to perform a division (a / b) and print the result.
a = 20
b = 10
division_result = a / b
print(division_result) # Output 2.0


# Using Variables and Types Casting
# Create a new variable c that stores the result of a divided by b. Make sure c is of type integer.
# Print the value and type of c.
# Now convert c to a float and print its new value and type.
a = 15
b = 12

# Divide a by b and make it an integer
c = int(a / b)

# Print value and type of c
print("c:", c) # Output c:1
print("type of c:", type(c)) # Output type of c: <class 'int'>

# Convert c to float
c = float(c)

# Print new value and type
print("new c:", c) # Output new c: 1.0
print("new type of c:", type(c)) # Output new type of c: <class 'float'>


# Working with String
# Declare a string variable message with the value The result of a divided by b is?
# Concatenate the message with the value of c, converted to a string and print the result.
a = 15
b = 12
c = int(a / b)

# Declare the message
message = "The result of a divided by b is "

# Concatenate and print
print(message + str(c)) # Output The result of a divided by b is 1


# Using Comparison Operators
# Compare if a is greater than b then and print the result True or False.
# Check if a is equal to b and print the result True or False.
a = 5
b = 2

# Check if a is greater than b
print(a > b) # Output True

# Check if a is equal to b
print(a == b) # Output False