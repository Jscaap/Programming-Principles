# 2.1.2 Exercise 1
'''
Student Profile - User class
1. Create a user profile by defining two core attributes first_name and last_name.
    This should include additional relevant details such as email, username,
    date_of_birth, location, and any other useful information.
    To display the user’s details, create a method called describe_user() that prints a
    clear and concise summary of the stored attributes. and now implement a method
    named greet_user() that provides a personalised welcome message including the
    user’s first name.
2. Create several instances representing different users, and call both methods for
    each user.
'''
class UserProfile:
    def __init__(self, first_name, last_name, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        
    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")

    def greet_user(self):
        print(f"Welcome {self.first_name}")
        
user1 = UserProfile(
    "Alice",
    "Smith",
    "sd1001@uni123st.edu.au",
    "Alice Smith"
)

user2 = UserProfile(
    "Bob",
    "Johnson",
    "sd1002@uni123st.edu.au",
    "Bob Johnson"
)

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()


# 2.1.3 Exercise 2
'''
Login Attempts
1. Add an attribute called login_attempts to your User class.
2. Write a method called increment_login_attempts() that increments the value of
    login_attempts by 1.
3. Write another method called reset_login_attempts() that resets the value of
    login_attempts to 0.
4. Make an instance of the User class and call increment_login_attempts() several
    times.
    Print the value of login_attempts to make sure it was correctly incremented, and
    then call reset_login_attempts(). Print login_attempts again to make sure it was
    reset to 0.
'''
class UserProfile:
    def __init__(self, first_name, last_name, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")

    def greet_user(self):
        print(f"Welcome {self.first_name}")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
user1 = UserProfile(
    "Alice",
    "Smith",
    "sd1001@uni123st.edu.au",
    "Alice Smith"
)

user2 = UserProfile(
    "Bob",
    "Johnson",
    "sd1002@uni123st.edu.au",
    "Bob Johnson"
)

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"Login Attempts: {user1.login_attempts}")

user1.reset_login_attempts

print(f"Login Attempt after reset: {user1.login_attempts}")


# 2.1.4 Exercise 3
'''
Student Profile - Classroom
1. Make a class called classroom. The init() method should store three attributes,
    classroom_name, classroom_location and seats_in_class. Make a method
    called describe_classroom() that prints these three pieces of information and a
    method called checksize_classroom() that prints a message indicating it has the
    number of seats needed from the course enrolled students.
2. Make an instance called classroom from your class. Print the three attributes
    ndividually, and then call both methods.
3. Create three different instances from the class and call describe_classroom() for
    each instance.
'''
class Classroom:
    def __init__(self, floor_number, classroom_location, seats_in_class):
        self.floor_number= floor_number
        self.classroom_location = classroom_location
        self.seats_in_class = seats_in_class
        
    def describe_classroom(self):
        print(f"Classroom Name: {self.floor_number}")
        print(f"Classroom Location: {self.classroom_location}")
        print(f"Seats in Class: {self.seats_in_class}")
        
    def checksize_classroom(self):
        print(f"This classroom has {self.seats_in_class} seats for enrolled students \n")
        
classroom1 = Classroom(
    "Ground Floor 101",
    "Building A",
    "15"
)

classroom2 = Classroom(
    "Ground Floor 105",
    "Building A",
    "25"
)

classroom1.describe_classroom()
classroom1.checksize_classroom()
classroom2.describe_classroom()
classroom2.checksize_classroom()


# 2.1.5 Exercise 4
'''
Enrolled Students
1. Add an attribute called students_enrolled with a default value of 0.
    Create an instance called classroom from this class. Print the number of students
    that have been enrolled, and then change this value and print it again.
2. Add a method called set_number_enrolled() to set the number of enrolled
    students.
    Call this method with a new number and print the value again.
3. Add a method called update_number_enrolled() that lets you change the number
    of enrolled students. Call this method with any number representing how many
    students are enrolled and create an audit log to capture a historical record of all
    changes. Include any other information you believe is relevant in the audit log.
'''
class Classroom:
    def __init__(self, classroom_name):
        self.classroom_name = classroom_name
        self.students_enrolled = 0
        self.audit_log = []

    def set_number_enrolled(self, number):
        self.students_enrolled = number
        self.audit_log.append(f"Set enrolled students to {number}")

    def update_number_enrolled(self, change):
        old_number = self.students_enrolled
        self.students_enrolled += change

        self.audit_log.append(
            f"Changed from {old_number} to {self.students_enrolled} "
            f"(change: {change})"
        )

classroom = Classroom("Python Programming")

print(f"Students enrolled: {classroom.students_enrolled}")

classroom.students_enrolled = 20
print(f"Updated students enrolled: {classroom.students_enrolled}")

classroom.set_number_enrolled(30)
print(f"Students enrolled after setting new value: {classroom.students_enrolled}")

classroom.update_number_enrolled(5)
print(f"Students enrolled after update: {classroom.students_enrolled}")

classroom.update_number_enrolled(-2)
print(f"Students enrolled after another update: {classroom.students_enrolled}")

print("\nAudit Log:")
for log in classroom.audit_log:
    print(log)


# 2.1.6 Exercise 5
'''
Classroom Equipment
1. The equipment class represents a collection of devices used within a classroom.
    Create a class called equipment that inherits from the classroom class.
2. Add an attribute named devices to store a list of classroom devices.
3. Implement a method that displays all devices stored in the list.
4. Create an instance of the Equipment class and call the method to display the
    devices.
'''
class Classroom:
    def __init__(self, classroom_name):
        self.classroom_name = classroom_name
        self.students_enrolled = 0

class Equipment(Classroom):
    def __init__(self, classroom_name):
        super().__init__(classroom_name)

        self.devices = [
            "Projector",
            "Laptop",
            "Printer",
            "Smart Board",
            "Speakers"
        ]

    def display_devices(self):
        print(f"Devices in {self.classroom_name} classroom:")

        for device in self.devices:
            print(device)

classroom_equipment = Equipment("Python Lab")

classroom_equipment.display_devices()
