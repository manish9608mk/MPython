'''
Inheritance

Inheritance allows one class to reuse the attributes and methods
of another class.

Key points:
- Parent class is also called Base class.
- Child class is also called Derived class.
- Child class inherits features from the parent class.
- Child class can add its own attributes and methods.
- It helps avoid writing the same code again.

Example:

Animal
├── eat()
└── sleep()

Dog
├── eat()      ← inherited
├── sleep()    ← inherited
└── bark()     ← Dog-specific

Cat
├── eat()      ← inherited
├── sleep()    ← inherited
└── meow()     ← Cat-specific

Real-world idea:
Animal contains common features.
Dog and Cat reuse those features and add their own behavior.
'''

# M1 - simple meaning of inheritance 
class Animal:
  def eat(self):
    print("I am eating")

  def sleep(self):
    print("I am sleeping")


class Dog(Animal):
  def bark(self):
    print("I am barking")

dog = Dog()

dog.bark()
dog.eat()      # Inherited from Animal
dog.sleep()    # Inherited from Animal

'''
Animal
  ↓
 Parent

Dog
  ↓
 Child

Dog gets:
    eat()
    sleep()

and adds:
    bark()
'''




print()
# M2 - Every Dog should have a name and age.
# It is better to put name and age in the Animal class.
# Then every child class that inherits from Animal will get them.
# We use __init__ to initialize these attributes.

class Animal:
  def __init__(self, name:str, age:int) -> None:
    self.name = name
    self.age = age 

  def eat(self):
    print('I am eating')

  def sleep(self):
    print('I am sleeping')

class Dog(Animal):
  def bark(self):
    print('I am barking')

  def display(self):
    print(f'Name is {self.name} and age is {self.age}')

dog = Dog('chika', 5)
dog.bark()
dog.eat()    
dog.sleep()  
dog.display()

'''
dog = Dog("Chika", 5)
Since Dog doesn't define its own __init__, Python uses the inherited Animal.__init__().

Dog object
   │
   ├── name = "Chika"    ← from Animal
   └── age = 5           ← from Animal

Methods:
   ├── bark()            ← Dog
   ├── display()         ← Dog
   ├── eat()             ← Animal
   └── sleep()           ← Animal
'''




print()
# M3 - The Dog has name and age, but now we also need a breed.
# Breed is specific to Dog, so we should not add it to Animal.
# Therefore, we add the breed attribute inside the Dog class.

class Animal:
  def __init__(self, name:str, age:int) -> None:
    self.name = name
    self.age = age 

  def eat(self):
    print('I am eating')

  def sleep(self):
    print('I am sleeping')

class Dog(Animal):
  def __init__(self, name:str, age:int, breed:str) -> None:
    super().__init__(name, age)
    self.breed = breed

  def bark(self):
    print('I am barking')

  def display(self):
    print(f'Name is {self.name}, age is {self.age} and breed is {self.breed}')

dog = Dog('chika', 5, 'bhopali')
dog.display()
dog.eat()
dog.sleep()
dog.bark()

dog = Dog("Chika", 5, "Bhopali")
print(dog.breed)       # ✅

animal = Animal("Tom", 10)
# print(animal.breed)    # ❌ AttributeError

'''
The key line: 
super().__init__(name, age)
means,
Call the parent's __init__() and let it initialize the attributes that belong to the parent.

Animal
├── name
├── age
├── eat()
└── sleep()

        ↑ inherited

Dog
├── name        ← inherited
├── age         ← inherited
├── eat()       ← inherited
├── sleep()     ← inherited
├── breed       ← Dog-specific
└── bark()      ← Dog-specific

'''




# Parent → common attributes
# Child  → common attributes + its own attributes
