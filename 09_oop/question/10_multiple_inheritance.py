'''
Multiple Inheritance

Multiple inheritance means a class inherits from
more than one parent class.

In this example:

    Battery ──┐
              ├──> ElectricCar
    Engine  ──┘

ElectricCar inherits from both Battery and Engine.

Important:
- A class can inherit from multiple classes.
- Syntax:
      class Child(Parent1, Parent2):
          ...
- The child class can use methods and attributes
  from both parent classes.
- Python uses MRO (Method Resolution Order) to decide
  which method to use when multiple parent classes
  have the same method.

Example:
    Battery → battery-related functionality
    Engine  → engine-related functionality
    ElectricCar → inherits from both
'''


class Battery:

  def battery_info(self):
    return 'Battery capacity: 85 KWh'


class Engine:

  def engine_info(self):
    return 'Electric motor'


# Multiple inheritance:
# ElectricCar inherits from both Battery and Engine.
class ElectricCar(Battery, Engine):

  def car_info(self):
    return 'This is an electric car'


tesla = ElectricCar()

print(tesla.car_info())
print(tesla.battery_info())
print(tesla.engine_info())