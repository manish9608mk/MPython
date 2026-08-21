'''
Polymorphism

Demonstrate polymorphism by defining the same method
fuel_type() in both Car and ElectricCar classes,
but with different behavior.

Car
└── fuel_type() → returns "Petrol"

ElectricCar
└── fuel_type() → returns "Electricity"

Same method name:
    fuel_type()

Different behavior:
    Car → Petrol
    ElectricCar → Electricity

This is achieved using Method Overriding.
'''




class Car:

  def __init__(self, brand: str, model: str) -> None:
    self.__car_brand = brand
    self.car_model = model

  def get_brand(self):
    return self.__car_brand + '!'

  def display(self) -> str:
    return f"Car details: {self.__car_brand}, {self.car_model}"

  def fuel_type(self):
    return 'Petrol or Diesel'

class ElectricCar(Car):

  def __init__(self, brand: str, model: str, battery_size: str) -> None:
    super().__init__(brand, model)

    self.battery_size = battery_size

  def fuel_type(self):
    return 'Electricity'  


my_tesla = ElectricCar("Tesla", "Model Y", "85KWH")
print(f'Fuel type: {my_tesla.fuel_type()}') # Fuel type: Electricity

safari = Car('Tata', 'safari')
print(f'Fuel type: {safari.fuel_type()}') # Fuel type: Petrol or Diesel


