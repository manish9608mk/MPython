"""
Class Method and self

Problem:
Add a method to the Car class that displays the
full name of the car (brand and model).

Example:
Brand = BMW
Model = M4

Output:
BMW M4
"""

class Car:
  wheel = 4  

  def __init__(self, brand:str, model:str) -> None:
    self.car_brand = brand
    self.car_model = model

  def display(self) -> str:
    return f"Car details: {self.car_brand} {self.car_model}, wheel = {Car.wheel}"

car1 = Car('BMW', 'M4')
print(f'Brand: {car1.car_brand}')   
print(f'Model: {car1.car_model}')   

print(car1.display())






'''

Car (Class)
│
└── wheel = 4          ← shared/class-level

car1 (Object)
├── car_brand = BMW    ← object-specific
└── car_model = M4    ← object-specific

car2 (Object)
├── car_brand = Tesla
└── car_model = Model Y


Class
  ↓
Blueprint

Object
  ↓
Actual instance

__init__
  ↓
Initialize object

self
  ↓
Current object

self.attribute
  ↓
Data belonging to that object
'''