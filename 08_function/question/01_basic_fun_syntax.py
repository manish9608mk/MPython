# Basic Function Syntax
# Create a function that takes a number as a parameter and returns its square.


# with return
def square(num):
  return num ** 2
print (square(8))

# without return
def square(num):
  print(num ** 2)
square(9)

# with user input 
def square (num):
  return num ** 2
num = int(input('Enter number: '))
print(square(num))

