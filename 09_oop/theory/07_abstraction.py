'''
Abstraction : 
Abstraction means exposing what an object does while hiding how it does it. or,

Abstraction means hiding complicated internal implementation
and showing only the necessary functionality to the user.

Key points:
- Hides unnecessary implementation details.
- Shows only the required functionality.
- Reduces complexity.
- Focuses on what an object does, not how it does it.

Real-life example:
When we use an ATM, we can:
    Withdraw
    Deposit
    Check Balance

We do not need to know how the ATM works internally.

In simple words:
    Abstraction = Hide the "how" and show the "what".
'''


# ABC and abstractmethod are used to create abstract classes.
from abc import ABC, abstractmethod


# Abstract class
class Shape(ABC):

  # Abstract method
  # Child classes must provide their own implementation.
  @abstractmethod
  def area(self):
    pass

  # Abstract method
  @abstractmethod
  def perimeter(self):
    pass


# Concrete class
# It inherits from Shape and implements all abstract methods.
class Rectangle(Shape):

  def __init__(self, length: int, breadth: int) -> None:
    self.length = length
    self.breadth = breadth

  def area(self):
    print(f'Area = {self.length * self.breadth}')

  def perimeter(self):
    print(f'Perimeter = {2 * (self.length + self.breadth)}')


r = Rectangle(5, 2)

r.area()
r.perimeter()


'''
Remember this for interviews

ABC
 ↓
Abstract Class
 ↓
Defines what child classes must do

@abstractmethod
 ↓
Method without implementation
 ↓
Child class must implement it

Concrete Class
 ↓
Provides actual implementation



One important point: You cannot create an object directly from Shape because it has abstract methods:
shape = Shape()   # TypeError

But you can create:
r = Rectangle(5, 2)   # correct
'''