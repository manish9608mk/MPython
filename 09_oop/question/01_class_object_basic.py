"""
Basic Class and Object

Problem:
Create a Car class with attributes like brand and model.
Then create an instance (object) of this class.
"""

class Car:
    
  def __init__(self, brand: str, model: str) -> None: 
    self.brand = brand
    self.model = model

car1 = Car("BMW", "M4")
print(f"Brand: {car1.brand}")
print(f"Model: {car1.model}")

car2 = Car("Tesla", "Y")
print(f"Brand: {car2.brand}")
print(f"Model: {car2.model}")

