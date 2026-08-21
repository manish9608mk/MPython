'''
Class Inheritance and isinstance()

Problem:
Demonstrate the use of isinstance() to check whether
my_tesla is an instance of Car and ElectricCar.

Important:
- isinstance(object, Class) checks whether an object
  belongs to a particular class.
- It returns True or False.
- Because ElectricCar inherits from Car, an ElectricCar
  object is also considered an instance of Car.

Example:

    my_tesla = ElectricCar(...)

    isinstance(my_tesla, ElectricCar)
        → True

    isinstance(my_tesla, Car)
        → True

Why?
    ElectricCar
        ↓ inherits from
    Car

So, an ElectricCar object is also a Car object.

In simple words:

    isinstance(object, Class)
        ↓
    "Is this object an instance of this class?"
'''


class Car:

  def __init__(self, brand: str, model: str) -> None:
    self.brand = brand
    self.model = model


class ElectricCar(Car):

  def __init__(self, brand: str, model: str, battery_size: str) -> None:
    super().__init__(brand, model)
    self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model Y", "85KWH")


# my_tesla is an ElectricCar object.
print(isinstance(my_tesla, ElectricCar))  # True

# ElectricCar inherits from Car,
# so my_tesla is also considered a Car object.
print(isinstance(my_tesla, Car))  # True


'''
Main thing to remember:

isinstance(object, Class)
        ↓
Checks whether the object belongs to that class
        ↓
Returns True or False


And because of inheritance:
ElectricCar → Car

my_tesla is ElectricCar → True
my_tesla is Car         → True

'''