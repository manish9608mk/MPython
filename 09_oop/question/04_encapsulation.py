"""
Encapsulation

Modify the Car class to encapsulate the
brand attribute, making it private, and
provide a getter method for it.

Car
├── private brand
└── get_brand() → safely access brand

Encapsulation :
Encapsulation means keeping data protected inside a class and providing controlled methods to access or modify that data. or, 
Encapsulation means hiding internal data and controlling how it is accessed.

In Python:
__brand
↓
Private attribute

get_brand()
↓
Getter method used to access the private data.
"""




class Car:

  def __init__(self, brand: str, model: str) -> None:
    self.__car_brand = brand
    self.car_model = model

  def get_brand(self):
    return self.__car_brand + '!'

  def display(self) -> str:
    return f"Car details: {self.__car_brand}, {self.car_model}"

class ElectricCar(Car):

  def __init__(self, brand: str, model: str, battery_size: str) -> None:
    super().__init__(brand, model)

    self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model Y", "85KWH")

# print(f"Brand: {my_tesla.__car_brand}") 
print(f"Brand: {my_tesla.get_brand()}")


'''
Car
├── __car_brand       ← private attribute
├── car_model         ← public attribute
└── get_brand()       ← getter

        ↑ inherits

ElectricCar
├── __car_brand       ← inherited private data exists,
│                       but cannot be accessed directly by child
├── car_model
├── get_brand()
└── battery_size

A child class can inherit a getter method that accesses private data defined by the parent class, but the child should not directly access the parent's __car_brand
'''