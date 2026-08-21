'''
==========================================
Constructor (__init__)
==========================================

A constructor is a special method inside a class.

It is automatically called when an object
(instance) of the class is created.

The constructor is mainly used to initialize
(assign initial values to) the object's attributes.

In Python, the constructor is written as:
__init__()

It is executed only once for each object,
at the time the object is created.

Syntax:

class ClassName:
    def __init__(self, parameters):
        self.attribute = parameter
'''

# Purpose:
# To initialize the object's state
# by assigning initial values to its attributes.


# Example: Student Class
# - __init__() initializes the student's data.
# - Each Student object has its own roll number,
#   name, and marks.
# - average() calculates and returns the average marks.

class Student:

    # Constructor
    def __init__(self, roll_no, name, marks):

        # Instance Variables
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    # Instance Method
    # Returns the average of all marks.
    def average(self):
        return sum(self.marks) / len(self.marks)


# Create a Student object.
first_student = Student(2, "Manish", [50, 60, 70, 80, 90])

# Access instance variables.
print(f"Name: {first_student.name}")

# Call an instance method.
print(f"Marks Average: {first_student.average()}")




'''
Q. What is a constructor?
Ans:
A constructor is a special method that is
automatically called when an object is created.
It is used to initialize the object's attributes.

Q. What is the constructor name in Python?
Ans:
__init__()

Q. Is __init__() called manually?
Ans:
No.
Python automatically calls it when an object
is created.

Q. How many times is __init__() called?
Ans:
Once for every object created.




One-line Revision:

Constructor (__init__)
        ↓
Runs Automatically
        ↓
Initializes Object Data
        ↓
Called Once Per Object
'''
