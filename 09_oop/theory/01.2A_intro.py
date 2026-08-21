print('--------------------------------------------------- Ex1')
# Ex1: Basic Class & Object
class Dog:

  def bark(self):
    print('Bhau Bhau!')
    print(self)

dog1 = Dog()
dog2 = Dog()

dog1.bark()
dog2.bark()



print('--------------------------------------------------- Ex2')
# Ex2: Constructor (init)
class Dog:

  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

  def bark(self):
    print('Bhau Bhau!')

dog1 = Dog('bihari dog', 'Blackbreed')
dog1.bark()
print(dog1.name)
print(dog1.breed)

dog2 = Dog('bhopali dog', 'Whitebreed')
dog2.bark()
print(dog2.name)
print(dog2.breed)




print('--------------------------------------------------- Ex3')
# Ex3: Object Inside Object (Composition)
class Dog:

  def __init__(self, name, breed, owner):
    self.name = name
    self.breed = breed
    self.owner = owner

  def bark(self):
    print('Bhau Bhau!')

class Owner:
  def __init__(self, name, address, contact_number):
    self.name = name
    self.address = address
    self.phone_number = contact_number

owner1 = Owner('manish', 'tokyo', '9608-9990')
dog1 = Dog('bihari dog', 'Blackbreed', owner1)
dog1.bark()
print(dog1.name)
print(dog1.breed)
print(dog1.owner.name)

owner2 = Owner('Sonu', 'france', '9444-4444')
dog2 = Dog('bhopali dog', 'Whitebreed', owner2)
dog2.bark()
print(dog2.name)
print(dog2.breed)
print(dog2.owner.address)

