print('--------------------------------------------------- Ex1')

# Example 1: Basic Class & Object
# - Create a class.
# - Create objects (instances) from the class.
# - Call a method using an object.
# - 'self' refers to the object that calls the method.

class Dog:

    def bark(self):
        print("Bhau Bhau!")

        # Print the current object (self)
        print(self)


# Create two different Dog objects.
dog1 = Dog()
dog2 = Dog()

# self = dog1
dog1.bark()

# self = dog2
dog2.bark()



print('--------------------------------------------------- Ex2')

# Example 2: Constructor (__init__)
# - __init__() runs automatically when an object is created.
# - It is used to initialize (assign) object data.
# - self.name and self.breed are instance variables.
# - Every object gets its own copy of these variables.

class Dog:

    def __init__(self, name, breed):

        # Store values inside the current object.
        self.name = name
        self.breed = breed

    def bark(self):
        print("Bhau Bhau!")


# Create the first Dog object.
dog1 = Dog("bihari dog", "Blackbreed")

dog1.bark()

print(dog1.name)
print(dog1.breed)


# Create the second Dog object.
dog2 = Dog("bhopali dog", "Whitebreed")

dog2.bark()

print(dog2.name)
print(dog2.breed)



print('--------------------------------------------------- Ex3')

# Example 3: Object Inside Object (Composition)
#
# Composition means:
# One object contains another object.
#
# Dog HAS-A Owner.
#
# Instead of storing only the owner's name,
# we store the entire Owner object inside Dog.

class Dog:

    def __init__(self, name, breed, owner):

        self.name = name
        self.breed = breed

        # Store the Owner object.
        self.owner = owner

    def bark(self):
        print("Bhau Bhau!")


class Owner:

    def __init__(self, name, address, contact_number):

        self.name = name
        self.address = address
        self.phone_number = contact_number


# Create an Owner object.
owner1 = Owner("Manish", "Tokyo", "9608-9990")

# Pass the Owner object to the Dog object.
dog1 = Dog("Bihari Dog", "Blackbreed", owner1)

dog1.bark()

print(dog1.name)
print(dog1.breed)

# Access the Owner object stored inside Dog.
print(dog1.owner.name)


# Create another Owner object.
owner2 = Owner("Sonu", "France", "9444-4444")

# Create another Dog object with a different owner.
dog2 = Dog("Bhopali Dog", "Whitebreed", owner2)

dog2.bark()

print(dog2.name)
print(dog2.breed)

# Access the owner's address.
print(dog2.owner.address)



'''
===========================================
Summary
===========================================

Class
↓
Blueprint (Template)

Object / Instance
↓
Real object created from a class

self
↓
Reference to the current object

__init__()
↓
Constructor
Runs automatically when an object is created.

Instance Variables
↓
Variables that belong to each object.
Each object has its own copy.

Composition
↓
One object contains another object.

Example:

Dog HAS-A Owner

dog1
│
▼
Dog Object
│
└────────► Owner Object

===========================================
Interview Notes

Q. What is self?
Ans:
self is a reference to the current object.

Q. What is __init__()?
Ans:
It is the constructor that automatically runs
when an object is created.

Q. What is an Instance Variable?
Ans:
A variable that belongs to a specific object.

Q. What is Composition?
Ans:
Composition is a HAS-A relationship where one
object contains another object.

===========================================
'''