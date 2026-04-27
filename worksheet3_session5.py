# Task 1 : Student Course Enrollment
'''
A university wants to track which courses its students are enrolled in. 
Create a dictionary called course_enrollments. 
Use student IDs as keys and store a list of course codes as values. 
Loop through the dictionary, printing each student's ID and their enrolled courses.
'''
course_enrollments = {
    1001: ["CS101", "MATH101"],
    1002: ["CS101", "MATH102"],
    1003: ["CS202", "PHY101"],
    1004: ["CS202", "CHEM101"],
    1005: ["BIO101", "HIST101"],
    1006: ["BIO102", "ENGL101"],
    1007: ["ECON101", "PSY101"],
    1008: ["ECON102", "SOC101"],
    1009: ["PSY102", "SOC102"],
    1010: ["CS101", "MATH101"]
}

for student_id, courses in course_enrollments.items():
    print(f"Student ID: {student_id}")
    print(f"Enrolled Courses: {courses}")
    print() # blank line for spacing


# Task 2 : Class Schedule
'''
A university wants to manage a list of all courses by department. 
Create a dictionary called departments.
Store these dictionary lists as tuples, where each tuple represents 
the department (e.g., (Department, CourseID and CourseName)). 
Loop through the dictionary, printing the courses for each department.
'''
departments = {
    "Computer Science": [
        ("Computer Science", "CS101", "Introduction to Computer Science"),
        ("Computer Science", "CS202", "Data Structures and Algorithms")
    ],
    "Mathematics": [
        ("Mathematics", "MATH101", "Calculus 1"),
        ("Mathematics", "MATH102", "Calculus 2")
    ],
    "Physics": [
        ("Physics", "PHY101", "General Physics 1"),
        ("Physics", "PHY102", "General Physics 2")
    ],
    "Chemistry": [
        ("Chemistry", "CHEM101", "General Chemistry 1"),
        ("Chemistry", "CHEM102", "General Chemistry 2")
    ],
    "Biology": [
        ("Biology", "BIO101", "Biology 1"),
        ("Biology", "BIO102", "Biology 2")
    ],
    "History": [
        ("History", "HIST101", "American History 1"),
        ("History", "HIST102", "American History 2")
    ],
    "English": [
        ("English", "ENGL101", "English Composition 1"),
        ("English", "ENGL102", "English Composition 2")
    ],
    "Economics": [
        ("Economics", "ECON101", "Principles of Economics"),
        ("Economics", "ECON102", "Intermediate Microeconomics")
    ],
    "Psychology": [
        ("Psychology", "PSY101", "Introduction to Psychology"),
        ("Psychology", "PSY102", "Developmental Psychology")
    ],
    "Sociology": [
        ("Sociology", "SOC101", "Introduction to Sociology"),
        ("Sociology", "SOC102", "Social Problems")
    ]
}

for dept, courses in departments.items():
    print(f"Department: {dept}")
    for course in courses:
        print(f"Course ID: , {course[1]}, | Course Name: , {course[2]}")
    print() # spacing


# Task 3 : Lecturer Assignments
'''
A university wants to track which lecturers are assigned to teach specific courses. 
Create a dictionary called lecturer_assignments. 
Use lecturer names as keys and store a list of course codes as values. 
Loop through the dictionary, printing each teacher's name and the courses they teach.
'''
lecture_assignments = {
    "Dr. Emily Brown": ["CS101", "MATH102"],
    "Mr. Michael Johnson": ["CS202", "PHY102"],
    "Asst. Prof. Olivia Taylor": ["MATH101", "CHEM101"],
    "Prof. David Lee": ["PHY101"],
    "Miss. Sophia Carter": ["CHEM102", "BIO101", "BIO102"],
    "Dr. Oliver Hernandez": ["HIST101", "HIST102", "ENGL101"],
    "Prof. Isabella Garcia": ["ENGL102", "SOC101"],
    "Prof. Evelyn Russell": ["ECON101", "ECON102"],
    "Dr. Lucas Sanchez": ["PSY101", "PSY102"],
    "Ass. Prof. Liam Lopez": ["SOC102"]
}

for lecturer, courses in lecture_assignments.items():
    print(f"Lecturer: {lecturer}")
    print(f"Courses: {courses}")
    print()