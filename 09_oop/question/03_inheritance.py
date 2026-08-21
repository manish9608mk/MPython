"""
Inheritance

Create an ElectricCar class that inherits from
the Car class and adds one new attribute:
battery_size.

Car
↓
Parent Class

ElectricCar
↓
Child Class

ElectricCar inherits the attributes and methods
of Car and adds its own battery_size attribute.

Example:

Car
├── brand
└── model

ElectricCar
├── brand      ← inherited
├── model      ← inherited
└── battery_size  ← new attribute

Inheritance helps us reuse existing code.
"""



class Car:

  def __init__(self, brand: str, model: str) -> None:
    self.car_brand = brand
    self.car_model = model

  def display(self) -> str:
    return f"Car details: {self.car_brand}, {self.car_model}"

class ElectricCar(Car):

  def __init__(self, brand: str, model: str, battery_size: str) -> None:
    # Call the Parent Class constructor.
    super().__init__(brand, model)

    # ElectricCar-specific attribute.
    self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model Y", "85KWH")

print(f"Brand: {my_tesla.car_brand}")
print(f"Model: {my_tesla.car_model}")
print(f"Battery size: {my_tesla.battery_size}")

# display() is inherited from Car.
print(f"{my_tesla.display()}, {my_tesla.battery_size}")


print()

car1 = Car("BMW", "M4")

print(f"Brand: {car1.car_brand}")
print(f"Model: {car1.car_model}")
print(car1.display())

# Car does not have the battery_size attribute.
# print(car1.battery_size)


'''
Car
├── car_brand
├── car_model
└── display()
        ↑
        │ inherited
        │
ElectricCar
├── car_brand
├── car_model
├── display()
└── battery_size   ← Child-specific

Most important interview point: super().__init__(brand, model) initializes the parent part of the ElectricCar object.
'''