'''
Property Decorator

Problem:
Use a property decorator in the Car class to make the
model attribute read-only.

Property
├── @property
├── Allows a method to be accessed like an attribute.
└── If no setter is defined, the attribute becomes read-only.

Important:
- @property is used to create a getter.
- We can access the property without calling it like a method.
- Example: car.model instead of car.model()
- If we do not define a setter, the property cannot be changed
  from outside the class.
- This is useful when we want to control access to an attribute.

Example:

    car.model
        ↓
    Calls the @property method

    car.model = "New Model"
        ↓
    Raises AttributeError if no setter is defined.

In simple words:

    @property
        ↓
    Method behaves like an attribute

    No @model.setter
        ↓
    Read-only property
'''


class Car:

  def __init__(self, brand: str, model: str) -> None:
    self.brand = brand
    self.__model = model

  @property
  def model(self):
    return self.__model


car = Car("Tesla", "Model Y")

# Access the model like an attribute.
print(car.model)

# Cannot modify the model because no setter is defined.
# car.model = "Model 3"   # AttributeError