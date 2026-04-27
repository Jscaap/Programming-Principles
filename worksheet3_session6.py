# Task 1: user input loop
'''
Write a code block that loop's and accepts input by entering the username. 
Enter the student's name to build a class list, 
and print a message saying you have added the student to their class. 
When you exit, print a list of all the students you input.
'''
students = []

while True:
    user_input = input("Enter student name or type 'exit to stop: ")
    
    if user_input == "exit":
        break
    
    students.append(user_input)
    print(f"{user_input} has been added to the class.")
    
print("\nClass List:")
for student in students:
    print(student)


# Task 2: locate rooms that can support
'''
Write a code block that accept's input and finds the minimum number 
of rooms with capacity to accommodate the number of students. 
Enter the minimum number of seats for the students attending the class. 
Print a message confirming the capacity, floor number and location.
'''
rooms = [
    (101, 15, "Ground Floor", "Building A"),
    (102, 15, "Ground Floor", "Building A"),
    (103, 20, "Ground Floor", "Building A"),
    (104, 20, "Ground Floor", "Building A"),
    (105, 25, "Ground Floor", "Building A"),
    (106, 25, "Ground Floor", "Building A"),
    (107, 30, "Ground Floor", "Building A"),
    (108, 30, "Ground Floor", "Building A"),
    (109, 30, "Ground Floor", "Building A"),
    (110, 10, "Ground Floor", "Building A"),
    (201, 10, "1st Floor", "Building A"),
    (202, 10, "1st Floor", "Building A"),
    (203, 25, "1st Floor", "Building A"),
    (204, 25, "1st Floor", "Building A"),
    (205, 30, "1st Floor", "Building A"),
    (206, 40, "1st Floor", "Building A"),
    (207, 40, "1st Floor", "Building A"),
    (208, 40, "1st Floor", "Building A")
]

students = int(input("Enter number of students: "))

best_room = None

for room in rooms:
    room_number, capacity, floor, location = room
    
    if capacity >= students:
        if best_room is None or capacity < best_room[1]:
            best_room = room

if best_room:
    print("\nRoom Assigned:")
    print(f"Room Number: {best_room[0]}")
    print(f"Capacity: {best_room[1]} seats")
    print(f"Floor: {best_room[2]}")
    print(f"Location: {best_room[3]}")
else:
    print("\nNo room available for this number of students.")


# Task 3: exit program loop
'''
Within your code block, to amend example 1 (User input loop) 
to create three different code blocks based on the following:
1.	Add a conditional test in a while loop to exit the program. 
    Exit parameters (quit, exit or 0), ensure that you print the names 
    of the students and the total number of students you have entered;
    also include the exit parameter.
2.	Use an active variable to control the loop's duration.
3.	Set a variable based on the room capacity. 
    Once you have entered the maximum number of students, t
    he program will exit using a break statement; upon exiting,
    print a list of students and the max_cap value.

'''
# Exit using condition (quit, exit, 0)
students = []

while True:
    name = input("Enter student name (or type quit/exit/0 to stop): ")
    
    if name.lower() in ["quit", "exit", "0"]:
        print(f"\nExit parameter used: {name}")
        break
    
    students.append(name)
    print(f"{name} has been added.")

print("\nStudent List:")
for student in students:
    print(student)

print(f"Total students: {len(students)}")

# Using an active variable
students = []
active = True

while active:
    name = input("Enter student name (or type exit to stop): ")
    
    if name.lower() == "exit":
        active = False
    else:
        students.append(name)
        print(f"{name} has been added.")

print("\nStudent List:")
for student in students:
    print(student)

print(f"Total students: {len(students)}")

# Exit when max room capacity is reached
students = []
max_cap = 5  # can change this number

while True:
    name = input("Enter student name: ")
    
    students.append(name)
    print(f"{name} has been added.")
    
    if len(students) == max_cap:
        print("\nMaximum capacity reached!")
        break

print("\nStudent List:")
for student in students:
    print(student)

print(f"Max capacity: {max_cap}")


# Task 4: Infinite Loop
'''
Create a code block that will loop after each input 
until you press CTRL-C to exit. Print each input on a 
new line and print the total number of lines.
'''
count = 0

try:
    while True:
        text = input("Enter something: ")
        print(text)
        count += 1

except KeyboardInterrupt:
    print("\n\nProgram interrupted (CTRL + C pressed)")

# After exiting
print(f"Total lines entered: {count}")