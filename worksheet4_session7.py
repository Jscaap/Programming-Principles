'''
1.1.2 Exercise 1
Student Registration
1. Define a Python function called course_enrollment() that registers a student for a
    new unit and prints a confirmation message for standard out (stdout). The
    message should include the student’s ID, first name, and last name, along with the
    course’s ID and course name.
2. Call the function using positional arguments to print the student and course
    information.
3. Call the function a second time using a keyword argument of Add, and if Add is not
    an argument that has been passed, then change the message to include the text
    Echo.
'''
def course_enrollment(student_id, first_name, last_name, course_id, course_name, action='Echo'):
    print(f"{action}: Student {student_id} | {first_name}, {last_name} is enrolled in {course_id} | {course_name}")
    
# default (Echo)
course_enrollment(101, "Jessica", "Putri", "ICT101", "Web Development")
# add
course_enrollment(101, "Jessica", "Putri", "ICT101", "Web Development", action="Add")
# amend
course_enrollment(101, "Jessica", "Putri", "ICT101", "Web Development", action="Amend")
# delete
course_enrollment(101, "Jessica", "Putri", "ICT101", "Web Development", action="Delete")


'''
1.1.3 Exercise 2
Student Course List
1. Define a Python function that allows input from standard in (stdin) to build a list of
    courses the student has enrolled in. The function should accept the student ID and
    name and then use a function that collects the course IDs. The function call will use
    the arguments student ID and name to summarise the courses enrolled. The
    function should collect four courses and the final action would be to confirm which
    semester and year.
2. Using the code from exercise 2.1 (above), write a function that stores information
    for each course (course ID and course name) in a dictionary. It should accept an
    arbitrary number of courses to populate the keyword arguments.
'''
# part 1
def collect_courses():
    courses = []
    
    for i in range(4):
        course_id = input(f"Enter course {i+1} ID: ") 
        # {i+1} mean take the current value of i which is 0, and add 1 so the UX look like "Enter course 1 ID" not "Enter course 0 ID"
        courses.append(course_id)
    return courses

def student_course_list(student_id, Student_name):
    courses = collect_courses()
    
    semester = input("Enter semester: ")
    year = input("Enter year: ")
    
    print("\n Enrollment Summary ")
    print(f"Student: {student_id} | {Student_name}")
    print("Courses enrolled: ")
    
    for course in courses:
        print(f"- {course}")
    print(f"Semester: {semester}, Year: {year}")
    
    
student_course_list(101, "Jessica Putri")

# part 2
def student_courses_dictionary(student_id, student_name, **courses):
    print("\n Course Dictionary ")
    print(f"Student: {student_id} | {student_name}")
    
    print("Courses enrolled: ")
    for course_id, course_name in courses.items():
        print(f"- {course_id}: {course_name}")
        
student_courses_dictionary(
    101,
    "Jessica Putri",
    ICT101="Web Development",
    ICT102="Python Programming",
    ICT103="Database Systems"
)


'''
1.1.4 Exercise 3
Tkinter calculator
Create a basic calculator using Python Tkinter to perform addition, subtraction,
multiplication, and division. The calculator should have two input fields for numbers and
a button to trigger the calculation. The result should be displayed in a separate label.
'''
import tkinter as tk

# --- Functions for operations ---
def add():
    result = float(entry1.get()) + float(entry2.get())
    result_label.config(text=f"Result: {result}")

def subtract():
    result = float(entry1.get()) - float(entry2.get())
    result_label.config(text=f"Result: {result}")

def multiply():
    result = float(entry1.get()) * float(entry2.get())
    result_label.config(text=f"Result: {result}")

def divide():
    try:
        result = float(entry1.get()) / float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ZeroDivisionError:
        result_label.config(text="Cannot divide by zero")


# --- Main window ---
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x250")


# --- Input fields ---
entry1 = tk.Entry(window)
entry1.pack(pady=5)

entry2 = tk.Entry(window)
entry2.pack(pady=5)


# --- Buttons ---
tk.Button(window, text="Add", command=add).pack(pady=5)
tk.Button(window, text="Subtract", command=subtract).pack(pady=5)
tk.Button(window, text="Multiply", command=multiply).pack(pady=5)
tk.Button(window, text="Divide", command=divide).pack(pady=5)


# --- Result label ---
result_label = tk.Label(window, text="Result: ")
result_label.pack(pady=10)


# --- Run app ---
window.mainloop()
