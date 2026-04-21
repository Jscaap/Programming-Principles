# using input() function
message = input("Enter a greeting message: ")
print(message)


# writing clear prompts
name = input("Please enter your name: ")
print(f"\nHello, {name}!")


# using int() -- False
# age = input("How old are you?")
# if age < 18:
#     print("Young")
    
    
# using int() -- Correct
age = int(input("How old are you? "))
if age < 18:
    print("Young")
    

# working with numbers
number = input("Enter a number: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even")
else:
    print(f"\nThe number {number} is odd")
    
    
# using while loop
current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1
    

# quitting loops
message = input("Enter a message or quit to exit")
while message != "quit":
    print(message)
    message = input("Enter another message or quit to exit")
    

# controlling loop execution
active = True
while active:
    message = input("Enter a message or quit to exit: ")
    if message == "quit":
        active = False
    else:
        print(message)


# using break to exit a loop
while True:
    number = int(input("Enter a number: "))
    if(number % 2 == 0):
        break
    else:
        print("Odd Number =", number) 
        
        
# using continue in a loop
number = 0
while number >= 0:
    number = int(input("Enter a number: "))
    if(number % 2 == 0):
        continue
    else:
        print("Odd Number =", number)
        

#  avoiding infinite loops
x = 1
while x <= 5:
    print(x)
    x += 1
 
# loop will run forever 
# x = 1
# while x <= 5:
#     print(x)

    
    
# finding value in the list
animals = ["dog", "cat", "rabbit", "hen"]
target = "hen"
i = 0
found = False
while i < len(animals):
    if animals[i] == target:
        found = True
        print(f"{target} found at index {i}")
        break
    i += 1
if not found:
    print(f"{target} not found in the list")
    
    
# removing all instances of specific values from a list
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)
while "cat" in pets:
    pets.remove("cat")
print(pets)


# filling a dictionary with user input
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    answer = input("Which mountain would you libe to climb someday?")
    responses[name] = answer
    
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Result ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")
    