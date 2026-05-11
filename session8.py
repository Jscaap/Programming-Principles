# creating and using a Class
class Dog:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def sit(self):
        print(f"{self.name} is now sitting")
    def roll_over(self):
        print(f"{self.name} rolled over")
        

# making an instance from a Class
class Dog:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def sit(self):
        print(f"{self.name} is now sitting")
    def roll_over(self):
        print(f"{self.name} rolled over")
        
my_dog = Dog("Willie, 6") # creating instance of class dog


# accessing attributes
# attributes
my_dog.name
my_dog.age
# methods
my_dog.sit()
my_dog.roll_over()


# accessing attributes
class Dog:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def sit(self):
        print(f"{self.name} is now sitting")
    def roll_over(self):
        print(f"{self.name} rolled over")
        
my_dog = Dog("Willie, 6") # creating instance of class dog

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")


# calling methods - multiple instances
my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()


# working with classes and instances
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name)


# setting a default value for an attribute
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
        
my_new_car = Car("audi", "a4", 2024)
my_new_car.read_odometer()


# modifying attribute values
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
        
my_new_car = Car("audi", "a4", 2024)
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# modifying attribute values - through a method
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
        
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
        
my_new_car = Car("audi", "a4", 2024)
my_new_car.update_odometer(23)
my_new_car.read_odometer()


# inheritance
# parent class
class Person:
    def speak(self):
        print("The person can speak")
        
# child class (inherits from person)
class Kid(Person):
    def play(self):
        print("The kids play with toys")
        
# create a instance of Person
my_kid = Kid()
my_kid.speak() # inherited from Person
my_kid.play() # defined in Kid


# inheritance - the init() method for a child class
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
        
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
        
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        
my_leaf = ElectricCar("nissan", "leaf", 2024)


# inheritance - defining attributes and methods for the child class
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 40
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size} -kWh battery")
        
my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name()) 
my_leaf.describe_battery()


# inheritance - overriding methods from the parent class
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 40
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size} -kWh battery")
        
    def get_descriptive_name(self):
        long_name = f"Electric car:{self.year} {self.make} {self.model}"
        return long_name
    
    
# importing classes - importing a single class
# car.py
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
        
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
        
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        
# my_car.py
from car import Car

my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name()) 
my_new_car.update_odometer(23)
my_new_car.read_odometer()

    
# importing classes - stroing multiple classes in a module
# car.py
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
        
# my_electric_car.py
from car import ElectricCar