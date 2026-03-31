# Worksheet 2, Session 4

# 5) Conditional Statement
units = [
    ("1", "computer_science"),
    ("2", "mathematics"),
    ("3", "computer_science"),
    ("4", "mathematics"),
    ("5", "physics"),
    ("6", "chemistry"),
    ("7", "biology"),
    ("8", "economics"),
    ("9", "economics"),
    ("10", "psychology"),
    ("11", "history"),
    ("12", "english"),
    ("13", "philosophy"),
    ("14", "mathematics"),
    ("15", "computer_science")
]

# 5.2.1 List of Departments
list_of_units = []

for unit in units:
    course_id = unit[0]
    department = unit[1]
    list_of_units.append((course_id, department))
    
print(list_of_units)    
    
# 5.2.2 Loops
while True:
    user_input = input("\n Enter course ID or 'quit' / 0 to exit: ")
    if user_input == "quit" or user_input == "0":
        print("Program ended")
        break
    
# 5.2.3 Conditional Statement
while True:
    user_input = input("\n Enter a course ID to find the department: ")

    if user_input == "quit" or user_input == "0":
        print("Program ended")
        break
    
    elif user_input:
        found = False
    
        for course_id, department in list_of_units:
            if course_id == user_input:
                print(f"Department: {department}")
                found = True
                break

        if found == False:
            print("Course ID not found")
            
    else :
        print("Invalid input, please enter a course ID")
        
# 5.2.4
while True:
    user_input = input("\n Enter a course ID (1 to 15) to check the name of department: ")
    
    if user_input == "0" or user_input == "quit":
        print(f"Course ID is out of range (1-15), try again: ")
    
    elif user_input in [str(i) for i in range(1,16)]:
        course_id = int(user_input)
        print(f"Course ID {course_id} is in the {list_of_units[course_id - 1]} department")
    
    else:
        print(f"The value {user_input} has been used to exit")
        break
       
# 5.3
# [course_id, course_name, department, prerequisites]
courses = [
    ["1", "introduction_to_programming", "computer_science", "none"],
    ["2", "calculus_1", "mathematics", "none"],
    ["3", "data_structures_and_algorithms", "computer_science", "introduction_to_programming"],
    ["4", "linear_algebra", "mathematics", "none"],
    ["5", "physics_1", "physics", "none"],
    ["6", "chemistry_1", "chemistry", "none"],
    ["7", "biology_1", "biology", "none"],
    ["8", "microeconomics", "economics", "none"],
    ["9", "macroeconomics", "economics", "microeconomics"],
    ["10", "psychology_1", "psychology", "none"],
    ["11", "history_1", "history", "none"],
    ["12", "english_composition_1", "english", "none"],
    ["13", "introduction_to_philosophy", "philosophy", "none"],
    ["14", "calculus_2", "mathematics", "calculus_1"],
    ["15", "discrete_mathematics", "computer_science", "introduction_to_programming"]
]
    
while True:
    user_input = input("\nEnter a course ID to retrieve course information (or '0' to quit): ")
    
    if user_input == "0":
        print("Exiting the program.")
        break

    found = False
    for course in courses:
        if course[0] == user_input:
            print(f"\nCourse ID: {course[0]}")
            print(f"Course Name: {course[1]}")
            print(f"Department: {course[2]}")
            print(f"Prerequisites: {course[3]}")
            found = True
            break
    
    if not found:
        print(f"The course ID {user_input} was not found.")