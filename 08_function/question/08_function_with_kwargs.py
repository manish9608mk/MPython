# Function with **kwargs
# Create a function that accepts any number
# of keyword arguments using **kwargs
# and prints them in the format:
# key: value

# Example:
# print_info(name="Mani", age=21)
# -> name: Mani
# -> age: 21


def employee(**details):
  for key, value in details.items():
    print(f'{key}: {value}')

employee(name ='Elon', company ='Tesla\n')  
employee(name ='Elon', company ='Tesla', networth ='Trillion\n')
employee(name ='Elon', company ='Tesla', networth ='Trillion', age ='50')    