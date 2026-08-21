'''
Class Variables

Problem:
Add a class variable to Car that keeps track of
the total number of cars created.

Car
├── total_car → shared by all Car objects
└── __init__() → increases total_car whenever a car is created

Important:
- total_car is a class variable.
- It is shared by all Car and ElectricCar objects.
- Every time a Car object is created, total_car increases by 1.
- ElectricCar also increases total_car because it calls
  super().__init__().
'''

class Car:

  # Class variable
  total_car = 0

  def __init__(self, brand: str, model: str) -> None:
    self.__car_brand = brand
    self.car_model = model

    # Increase the shared class variable
    Car.total_car += 1

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
safari = Car("Tata", "Safari")
nexon = Car("Tata", "Nexon")

print(f"Tesla fuel type: {my_tesla.fuel_type()}")
print(f"Safari fuel type: {safari.fuel_type()}")

print(f"Total cars created: {Car.total_car}")


# O/P
#Tesla fuel type: Electricity
# Safari fuel type: Petrol or Diesel
# Total cars created: 3


'''
Why is the count 3?

my_tesla = ElectricCar(...)
        ↓
super().__init__()
        ↓
Car.__init__()
        ↓
Car.total_car = 1

safari = Car(...)
        ↓
Car.total_car = 2

nexon = Car(...)
        ↓
Car.total_car = 3

'''








print()
# in detailed 

'''
Class Variables

A class variable is a variable that belongs to the class
rather than to a particular object.

It is shared by all objects created from that class.

Problem:
Add a class variable to Car that keeps track of
the total number of cars created.

Car
├── total_car → class variable shared by all objects
├── __car_brand → instance variable
└── car_model → instance variable

Important:
- total_car is defined directly inside the Car class.
- It is shared by all Car objects.
- It is also shared by ElectricCar objects because ElectricCar
  inherits from Car.
- Every time a new Car object is created, total_car increases by 1.
- ElectricCar also increases total_car because its __init__()
  calls super().__init__(), which executes Car.__init__().
- Use Car.total_car to access the class variable.

Real-world example:
A car company wants to know how many cars have been created.
Instead of storing the count separately inside every car object,
we keep one shared variable:

    Car.total_car

In simple words:

    Class variable
        ↓
    Shared by all objects

    Instance variable
        ↓
    Separate for each object
'''

class Car:

  # Class variable
  # Shared by all Car objects
  total_car = 0

  def __init__(self, brand: str, model: str) -> None:
    # Instance variables
    # Each object gets its own brand and model
    self.__car_brand = brand
    self.car_model = model

    # Increase the shared class variable
    # This runs every time a new Car object is created.
    Car.total_car += 1

  def get_brand(self):
    return self.__car_brand + '!'

  def display(self) -> str:
    return f"Car details: {self.__car_brand}, {self.car_model}"

  def fuel_type(self):
    return 'Petrol or Diesel'


class ElectricCar(Car):

  def __init__(self, brand: str, model: str, battery_size: str) -> None:

    # Calls the parent class __init__()
    # This initializes the Car attributes and also
    # increases Car.total_car by 1.
    super().__init__(brand, model)

    self.battery_size = battery_size

  def fuel_type(self):
    return 'Electricity'


# Creating an ElectricCar object
# super().__init__() calls Car.__init__()
# Therefore, Car.total_car becomes 1.
my_tesla = ElectricCar("Tesla", "Model Y", "85KWH")

# Creating a Car object
# Car.__init__() runs and Car.total_car becomes 2.
safari = Car("Tata", "Safari")

# Creating another Car object
# Car.__init__() runs and Car.total_car becomes 3.
nexon = Car("Tata", "Nexon")


print(f"Tesla fuel type: {my_tesla.fuel_type()}")
print(f"Safari fuel type: {safari.fuel_type()}")

# Accessing the class variable using the class name
print(f"Total cars created: {Car.total_car}")


# O/P
# Tesla fuel type: Electricity
# Safari fuel type: Petrol or Diesel
# Total cars created: 3


'''
Why is the count 3?

1. Creating my_tesla:

    my_tesla = ElectricCar(...)
              ↓
    ElectricCar.__init__()
              ↓
    super().__init__()
              ↓
    Car.__init__()
              ↓
    Car.total_car += 1
              ↓
    Car.total_car = 1


2. Creating safari:

    safari = Car(...)
            ↓
    Car.__init__()
            ↓
    Car.total_car += 1
            ↓
    Car.total_car = 2


3. Creating nexon:

    nexon = Car(...)
           ↓
    Car.__init__()
           ↓
    Car.total_car += 1
           ↓
    Car.total_car = 3


Final result:

    Car.total_car = 3

Because we created 3 objects in total:

    1. my_tesla → ElectricCar
    2. safari   → Car
    3. nexon    → Car

So the class variable keeps track of
the total number of objects created.
'''







