'''
Static Method

A static method is a method that does not depend on
a specific object or the class itself.

It does not use:
    self → current object
    cls  → current class

Use @staticmethod when the method performs a general task
and does not need object data or class data.

Example:
    general_definition()
    → returns general information about a car.

Important:
- Static method uses @staticmethod.
- It does not take self or cls.
- It cannot directly access instance variables.
- It cannot directly access class variables.
- It can be called using the class name or an object.

In simple words:

    Instance method
        ↓
    Uses object data → self

    Class method
        ↓
    Uses class data → cls

    Static method
        ↓
    General task → no self, no cls
'''


class Car:

  total_car = 0

  def __init__(self, brand: str, model: str) -> None:
    self.__car_brand = brand
    self.car_model = model

    Car.total_car += 1

  def get_brand(self):
    return self.__car_brand + '!'

  def display(self) -> str:
    return f"Car details: {self.__car_brand}, {self.car_model}"

  def fuel_type(self):
    return 'Petrol or Diesel'

  # Static method
  # Does not use self or cls because it does not need
  # object-specific or class-specific data.
  @staticmethod
  def general_definition():
    return 'Cars are means of transport'


class ElectricCar(Car):

  def __init__(self, brand: str, model: str, battery_size: str) -> None:
    super().__init__(brand, model)

    self.battery_size = battery_size

  def fuel_type(self):
    return 'Electricity'


safari = Car("Tata", "Safari")

# Static method can be called using an object.
print(safari.general_definition())

# Preferred way: call a static method using the class name.
print(Car.general_definition())


'''
For the previous question, the important parts were:

@staticmethod
No self
No cls
Does not depend on object data or class data

Can be called as:
Car.general_definition()

Know the difference:
Instance method → self → object
Class method    → cls  → class
Static method   → neither → independent utility
'''