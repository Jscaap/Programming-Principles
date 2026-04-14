# if statement example
number = 10
if (number==0):
    print("Number is equal to 0")
    

# if else statement example
number = 10
if (number==0):
    print("Number is equal to 0")
else:
    print(f"Number is {number}")
    

# multiple elif blocks
age = 70
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"price {price}")


# testing multiple conditions
toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in toppings:
    print("Adding mushrooms")
if "extra cheese" in toppings:
    print("Adding extra cheese")
    

# loops and conditional statements
toppings = ["mushrooms", "green peppers", "extra cheese"]
for topping in toppings:
    print(f"Adding {topping}")
    
for topping in toppings:
    if topping == "green peppers":
        print("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {topping}")
        
    
# checking for empty lists before looping
toppings = []
if toppings:
    for topping in toppings:
        print(f"Adding {topping}")
else:
    print("Are you sure you want a plain pizza?")
    
    
# validating inputs againts a set of values
available_toppings = ["mushrooms", "olives", "green peppers", "extra cheese"]
requested_toppings = ["mushrooms", "french fries"]
for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping}")
    else:
        print(f"Sorry, we dont have {topping}")