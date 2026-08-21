"""
========================================================
Class Method, self, Instance Variables & Class Variables
========================================================

Problem:
Create a Car class with:
    - brand
    - model

Add a method that displays the full car details.

We will also use a class variable:
    - wheel = 4
"""


class Car:

    # --------------------------------------------------
    # Class Variable
    # --------------------------------------------------
    # 'wheel' belongs to the CLASS, not to one particular
    # car object.
    #
    # All Car objects can access this value.
    wheel = 4


    # --------------------------------------------------
    # Constructor
    # --------------------------------------------------
    # __init__() is automatically called when we create
    # a new Car object.
    #
    # self   -> current object
    # brand  -> value provided while creating the object
    # model  -> value provided while creating the object
    #
    # -> None means this method does not return a value.
    def __init__(self, brand: str, model: str) -> None:

        # Instance Variables
        #
        # These variables belong to the specific object.
        #
        # Example:
        # car1.car_brand -> "BMW"
        # car1.car_model -> "M4"

        self.car_brand = brand
        self.car_model = model


    # --------------------------------------------------
    # Instance Method
    # --------------------------------------------------
    # This method works with a particular Car object.
    #
    # self represents the object on which the method
    # is called.
    def display(self) -> None:

        # self.car_brand  -> instance variable
        # self.car_model  -> instance variable
        #
        # Car.wheel -> class variable
        print(
            f"Car details: "
            f"{self.car_brand} {self.car_model}, "
            f"wheel = {Car.wheel}"
        )


# ======================================================
# Create an Object
# ======================================================

# Car(...) creates a new object.
#
# "BMW" is passed to brand
# "M4" is passed to model
#
# Python automatically calls:
#
# Car.__init__(car1, "BMW", "M4")
#
# Therefore:
#
# car1.car_brand = "BMW"
# car1.car_model = "M4"

car1 = Car("BMW", "M4")


# ======================================================
# Access Instance Variables
# ======================================================

# car1 has its own car_brand and car_model.
print(f"Brand: {car1.car_brand}")
print(f"Model: {car1.car_model}")


# ======================================================
# Call Instance Method
# ======================================================

# Calling:
#
#     car1.display()
#
# is conceptually similar to:
#
#     Car.display(car1)
#
# Therefore inside display():
#
#     self = car1

car1.display()




'''
CLASS
  ↓
Blueprint
  ↓
creates
  ↓
OBJECT
  ↓
has its own
  ↓
INSTANCE VARIABLES

self
  ↓
Current Object

__init__()
  ↓
Initialize Object

INSTANCE METHOD
  ↓
Works with Object

CLASS VARIABLE
  ↓
Belongs to Class

'''








# or
print()

"""
=========================================================
Question: Class Method and self
=========================================================

Problem:
Add a method to the Car class that displays the
full name of the car (brand and model).

Example:

Brand = BMW
Model = M4

Output:
BMW M4

Concepts covered:
- Class
- Object / Instance
- Constructor (__init__)
- self
- Instance Variables
- Class Variables
- Instance Method
- return
- Type Hints
"""


# =======================================================
# Class Definition
# =======================================================

class Car:

    # ---------------------------------------------------
    # Class Variable
    # ---------------------------------------------------
    # 'wheel' is a class variable.
    #
    # It belongs to the Car class rather than to one
    # specific Car object.
    #
    # All Car objects can access this value.
    #
    # We can access it using:
    #
    # Car.wheel
    #
    # Example:
    # Car.wheel -> 4

    wheel = 4


    # ---------------------------------------------------
    # Constructor
    # ---------------------------------------------------
    # __init__() is a special method that Python calls
    # automatically when a new Car object is created.
    #
    # Parameters:
    #
    # self  -> reference to the current object
    # brand -> value passed while creating the object
    # model -> value passed while creating the object
    #
    # -> None means this method does not return a value.

    def __init__(self, brand: str, model: str) -> None:

        # ------------------------------------------------
        # Instance Variables
        # ------------------------------------------------
        # Instance variables belong to a specific object.
        #
        # self.car_brand stores the brand inside the
        # current Car object.
        #
        # self.car_model stores the model inside the
        # current Car object.
        #
        # Example:
        #
        # car1 = Car("BMW", "M4")
        #
        # Then:
        #
        # car1.car_brand -> "BMW"
        # car1.car_model -> "M4"

        self.car_brand = brand
        self.car_model = model


    # ---------------------------------------------------
    # Instance Method
    # ---------------------------------------------------
    # display() is an instance method because it works
    # with the data of a particular Car object.
    #
    # self represents the current object.
    #
    # -> str means this method returns a string.

    def display(self) -> str:

        # Return the car details instead of directly
        # printing them.
        #
        # self.car_brand -> instance variable
        # self.car_model -> instance variable
        #
        # Car.wheel -> class variable
        #
        # The caller can decide what to do with the
        # returned string.
        #
        # For example:
        #
        # print(car1.display())

        return f"Car details: {self.car_brand} {self.car_model}, wheel = {Car.wheel}"


# =======================================================
# Creating an Object
# =======================================================

# Car("BMW", "M4") creates a new Car object.
#
# Python automatically calls:
#
# Car.__init__(car1, "BMW", "M4")
#
# Conceptually:
#
# self = car1
# brand = "BMW"
# model = "M4"
#
# Therefore:
#
# car1.car_brand = "BMW"
# car1.car_model = "M4"

car1 = Car("BMW", "M4")


# =======================================================
# Accessing Instance Variables
# =======================================================

# car1 has its own car_brand value.
print(f"Brand: {car1.car_brand}")

# car1 has its own car_model value.
print(f"Model: {car1.car_model}")


# =======================================================
# Calling Instance Method
# =======================================================

# Call the display() method using car1.
#
# When we write:
#
# car1.display()
#
# Python conceptually passes car1 as self:
#
# Car.display(car1)
#
# Therefore inside display():
#
# self == car1
#
# So:
#
# self.car_brand
# means:
# car1.car_brand
#
# and:
#
# self.car_model
# means:
# car1.car_model

print(car1.display())


"""
=========================================================
Object Structure
=========================================================

Car (Class / Blueprint)
│
├── wheel = 4
│      ↑
│      Class Variable
│
└── creates objects
       │
       └── car1 (Object / Instance)
            │
            ├── car_brand = "BMW"
            │       ↑
            │       Instance Variable
            │
            └── car_model = "M4"
                    ↑
                    Instance Variable


=========================================================
Class vs Object
=========================================================

Class
↓
Blueprint / Template

Object
↓
Actual instance created from the class


Example:

class Car:
    ...
        ↓
     Blueprint

car1 = Car("BMW", "M4")
        ↓
     Actual Object


=========================================================
__init__()
=========================================================

__init__()
↓
Automatically called when object is created
↓
Initializes object data
↓
Assigns values to instance variables


Example:

car1 = Car("BMW", "M4")

        ↓

__init__(self, "BMW", "M4")

        ↓

self.car_brand = "BMW"
self.car_model = "M4"


=========================================================
self
=========================================================

self
↓
Reference to the current object


car1.display()

        ↓

Car.display(car1)

        ↓

self = car1


Therefore:

self.car_brand
        ↓
car1.car_brand

self.car_model
        ↓
car1.car_model


=========================================================
Instance Variable
=========================================================

self.car_brand
self.car_model

↓
Belong to a specific object.

Example:

car1.car_brand = "BMW"

car2.car_brand = "Tesla"

Each object can have different values.


=========================================================
Class Variable
=========================================================

Car.wheel

↓
Belongs to the class.

Example:

Car.wheel
↓
4

Multiple objects can access it.


=========================================================
return vs print
=========================================================

return
↓
Sends a value back to the caller
↓
Caller decides what to do with it


print()
↓
Displays something on the screen


Therefore:

def display(self) -> str:
    return "BMW M4"

is more reusable than:

def display(self):
    print("BMW M4")


Example:

details = car1.display()

print(details)


=========================================================
One-Line Revision
=========================================================

Class
↓
Blueprint

Object
↓
Actual Instance

__init__()
↓
Initialize Object

self
↓
Current Object

self.attribute
↓
Instance Data

Class Variable
↓
Shared Class-Level Data

Instance Method
↓
Method that works with an Object

return
↓
Give Result Back to Caller



class Car
    ↓
Blueprint
    ↓
Car("BMW", "M4")
    ↓
New Object
    ↓
__init__()
    ↓
self = car1
    ↓
self.car_brand = "BMW"
self.car_model = "M4"
    ↓
car1.display()
    ↓
Car.display(car1)
    ↓
self = car1
    ↓
return car1.car_brand + car1.car_model
"""

