# Worksheet 2, Session 3

# 2) Lists
# print 15 courses from table units to create a list in any order
units = ["introduction_to_programming",
         "calculus_1", 
         "data_structures_and_algorithms", 
         "linear_algebra", 
         "physics_1", 
         "chemistry_1", 
         "biology_1", 
         "microeconomics", 
         "macroeconomics", 
         "psychology_1", 
         "history_1", 
         "english_composition", 
         "introduction_to_philosophy", 
         "calculus_2", 
         "discrete_mathematics"]
print ("the list of the units are: ", units)


# use sorted() to sort the list alphabetically and print the list
sorted_units = sorted(units)
print ("\nthe list of the units in alphabetical order: ", sorted_units)


# use reverse() to reverse the list twice and print the list
units.reverse()
print ("\nreversed list: ", units) #reverse the list
units.reverse()
print ("\noriginal order again: ", units) #reverse back to original


# use sort() to sort the list alphabetically, use sort() to change the list and store it in reverse alphabetical order
units.sort()
print ("\nsort list alphabetically: ", units) #sort units alphabetically using sort()
units.sort(reverse=True)
print ("\nsort list reverse alphabetical order: ", units) #sort units in reverse alphabetical order


# 2.1) Lists - Create useable coding
# use sort() to set the order the list alphabetically without changing the original list and print a announcement message
courses = ["introduction_to_programming",
                "calculus_1", 
                "data_structures_and_algorithms", 
                "linear_algebra", 
                "physics_1", 
                "chemistry_1", 
                "biology_1", 
                "microeconomics", 
                "macroeconomics", 
                "psychology_1", 
                "history_1", 
                "english_composition", 
                "introduction_to_philosophy", 
                "calculus_2", 
                "discrete_mathematics"
                ]
print (f"\nThe following courses are available for expression of interest if the students meet the prerequisited: {sorted(courses)}\n")


# remove one course from the courses list, replace it with a new course and print messages showing the original course, new course and confirmation messages
withdrawn_course = courses[1] # calculus_1
new_course = "accounting"
courses[1] = new_course

print(f"\nOriginal course withdrawn : {withdrawn_course}\n")
print(f"New course added : {new_course}\n")
print(f"The course {withdrawn_course} has been withdrawn. It has been replaced with {new_course}\n")
print(f"Updated course list : {courses}\n")


# use insert() and append() to add new courses on the list and print the messages showing the available courses
new_course_start = courses.insert(0, "mandarin_language") # add course in the beginning of the list

new_course_middle = len(courses) // 2
courses.insert(new_course_middle, "cyber_security") # add course in the middle of the list

new_course_end = courses.append("business_analyst") # add course in the end of the list

print(f"Available courses in this semester: {courses}\n")


# remove four courses from the list using pop() due to technical and rom availability issues, prinnt the message
unavailable_course_1 = courses.pop(1) # remove second course
unavailable_course_2 = courses.pop(-1) # remove last course
unavailable_course_3 = courses.pop(2) # remove third course
print(f"The following courses are unavailable due to technical and room availability issues: \n {unavailable_course_1} \n {unavailable_course_2} \n {unavailable_course_3}\n \n These courses have been successfully withdrawn\n")
print(f"Available courses: {courses}\n")


# 3) Tuples and Loops
# create a list of tuples containing course IDs and names, loop through each tuple to extract the information, store it in a new list, and then print the course details
courses_id_courses_name = [
    ("001", "introduction_to_programming"),
    ("002", "calculus_1"),
    ("003", "data_structure_and_algorithms")
]

courses_id_courses_name_list = []
for course in courses_id_courses_name:
    course_id = course[0]
    course_name = course[1]
    courses_id_courses_name_list.append((course_id, course_name))
    
print("Course Information:")
for item in courses_id_courses_name_list:
    print("ID:", item[0], "| Name:", item[1])
    
# for course_id, course_name in courses: 
#     course_list.append((course_id, course_name))