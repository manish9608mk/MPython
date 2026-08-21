# Polymorphism in Functions
# Create a function that multiplies two values.
# The function should work with both numbers and strings.
# Example:
# multiply(3, 4)      -> 12
# multiply("Hi", 3)   -> "HiHiHi"

'''
Why is this called Polymorphism?
- Because the same function behaves differently depending on the type of arguments passed to it.

multiply(3, 4)      # Multiplies numbers
multiply("Hi", 3)   # Repeats the string

The function name is the same (multiply), but the behavior changes based on the input type. This is called polymorphism in Python.
'''


# ex1 - without user input  

def multiply(a,b):
  return a * b

print(multiply(3,5))
print(multiply(3,'Hi '))


