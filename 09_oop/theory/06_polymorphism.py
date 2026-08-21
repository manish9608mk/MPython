'''
Polymorphism

Poly = many
Morph = forms

Polymorphism means the same method name can behave differently
depending on which object calls it.

Key points:
- The same method name can have different behavior.
- Different classes can provide their own implementation of the method.
- It makes code flexible and easier to extend.
- A child class can override a method of its parent class.

Example:

Circle
└── draw() → draws a circle

Rectangle
└── draw() → draws a rectangle

Same method name:
    draw()

Different behavior:
    Circle → draws a circle
    Rectangle → draws a rectangle

This is called Method Overriding.
'''

class Animal:
  def __init__(self, name: str, age: int) -> None:
    self.name = name
    self.age = age 

  def eat(self):
    print('I am eating')

  def sleep(self):
    print('I am sleeping')

  def move(self):
    print('Animal class - I am moving')


class Dog(Animal):
  def __init__(self, name: str, age: int, breed: str) -> None:
    super().__init__(name, age)
    self.breed = breed

  def bark(self):
    print('I am barking')

  def display(self):
    print(
      f'Name is {self.name}, '
      f'age is {self.age} and '
      f'breed is {self.breed}'
    )


dog = Dog('Chika', 5, 'Bhopali')
dog.move()


print()

# If the child class defines a method with the same name
# as the parent class, the child version overrides the parent version.
# This is called Method Overriding.

class Animal:
  def __init__(self, name: str, age: int) -> None:
    self.name = name
    self.age = age 

  def eat(self):
    print('I am eating')

  def sleep(self):
    print('I am sleeping')

  def move(self):
    print('Animal class - I am moving')


class Dog(Animal):
  def __init__(self, name: str, age: int, breed: str) -> None:
    super().__init__(name, age)
    self.breed = breed

  def bark(self):
    print('I am barking')

  def display(self):
    print(
      f'Name is {self.name}, '
      f'age is {self.age} and '
      f'breed is {self.breed}'
    )

  # Method overriding
  def move(self):
    print('Dog class - I am running on 4 legs')


dog = Dog('Chika', 5, 'Bhopali')
dog.move()
# O/P - Dog class - I am running on 4 legs

'''
One important interview point

When you do:

dog.move()

Python looks for move() in the Dog class first.

dog.move()
   ↓
Does Dog have move()?
   ↓
YES
   ↓
Use Dog.move()

If Dog didn't have move():

dog.move()
   ↓
Does Dog have move()?
   ↓
NO
   ↓
Check Parent (Animal)
   ↓
Animal.move()

This is the foundation for understanding method overriding, polymorphism, and later MRO (Method Resolution Order).
MRO
    ↓
Order Python follows to find that method
'''