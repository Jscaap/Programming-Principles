# functions 
def greet_user():
    print("Hello!")

greet_user() # function call


# passing arguments
# functions can take inputs or parameters to perform task based on those inputs
def greet_user(username):
    print(f"Hello, {username}!")
    
greet_user("John")

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}")
    
describe_pet("cat", "Mano")  
describe_pet("dog", "Tomy")


# keyword arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}")
    
describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="harry", animal_type="hamster")


# default values
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
    
describe_pet("Tommy")
describe_pet(pet_name="Mano", animal_type="cat")


# returning a simple value
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name

musician = get_formatted_name("Jony", "Tim")
print(musician)


# making an argument optional
def get_formatted_name(first_name, last_name, middle_name=''):
    # middle_name = '' it has a default value, so it becomes optional
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name

musician = get_formatted_name("Jimi", "Hendrix")
print(musician)

musician = get_formatted_name("John", "Hooker", "Lee")
print(musician)


# returning a dictionary
def build_person(first_name, last_name, age=None):
    person = {"first: first_name", "last: last_name"}
    if age:
        person["age"] = age
    return person

musician = build_person("Jimi", "Hendrix", age = 27)
print(musician)


# function with a while loop
while True:
    print("Please tell me your name, Enter 'q' at any time to quit:")
    
    first_name = input("First name: ")
    if first_name == 'q':
        break
    
    last_name = input("Last name: ")
    if last_name == 'q':
        break
    
    name = get_formatted_name(first_name, last_name)
    print(f"Hello, {name}!")
    

# passing a list to the function
def greet_user(names):
    for name in names:
        message = f"Hello, {name}!"
        print(message)

usernames = ["Hannah", "Tina", "John"]
greet_user(usernames)


# modifying a list in a function
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)
    
unprinted_designs = ["phone case", "robot pendant", "flowers"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# arbitrary number of arguments
def make_pizza(*toppings):
    print("\nmaking a pizza with the follwowing toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


# mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    print(f"\nMaking a {size} - inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# arbitrary keyword arguments
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("albert", "einstein", location = "princeton", field = "physics")
print(user_profile)


# importing an entire module
# def make_pizza(size, *toppings):
#     print(f"\nmaking a {size} - inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
#  import pizza
# pizza.make_pizza(16, "pepperoni")
# pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# importing all functions in a module
# from pizza import *
# make_pizza(16, "pepperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")