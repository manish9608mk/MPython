'''
One-line revision:

Class        → Blueprint
Object       → Real instance
Attribute    → What object has
Method       → What object does
Constructor  → Initializes object
self         → Current object
Encapsulation→ Bundle + control access
Inheritance  → Reuse parent features
Polymorphism → Same interface, different behavior
Abstraction  → Hide complexity
Overriding   → Child changes parent method
Composition  → HAS-A
Association  → Related objects
Aggregation  → HAS-A, independent objects
'''


# A class is a blueprint (template) used to create objects.
# An instance is a real object created from that class.

# Class (Blueprint)
class Car:

    # Constructor: Runs automatically when an object is created.
    def __init__(self, brand, color):

        # Instance Variables:
        # Each object gets its own copy of these variables.
        self.brand = brand
        self.color = color


# Creating Objects (Instances)
car1 = Car("Tesla", "Red")      # Instance 1
car2 = Car("BMW", "Silver")     # Instance 2

print(car1.brand)   # Tesla
print(car2.brand)   # BMW




print()

# Example: Basic Class Variable
# - x is a class variable.
# - It belongs to the class, not to a specific object.
# - All objects of the class can access the same class variable.

class First:

    # Class Variable
    x = 50


# Create an object (instance) of the class.
obj = First()

# Access the class variable using the object.
print(obj.x)      # Output: 50

