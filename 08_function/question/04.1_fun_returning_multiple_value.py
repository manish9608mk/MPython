# Function Returning Multiple Values
# Create a function that takes the radius of a circle as a parameter
# and returns both the area and circumference of the circle.
#
# Formula:
# Area = π × r²
# Circumference = 2 × π × r
# Here we use Python's math library.

import math


# ex1

def circle(radius):

  area = math.pi * (radius) ** 2
  circumference = 2 * math.pi * radius

  return area, circumference

area_circle , circumference_circle = circle(4)   # Receive the returned values using tuple unpacking.

print("Area:", area_circle)
print("Circumference:", circumference_circle)



# with precision output : 
print()

# Method 1 recommended 
print(f'area of circle with precision M1 : {area_circle: .2f}')
print(f'area of circle with precision M1 : {circumference_circle: .5f}')
'''
.2f meaning
.
↓
Decimal point

2
↓
2 digits after decimal

f
↓
Floating-point number
'''

# Method 2
print('area M2 : ', round(area_circle, 2)) 
print('circumference M2 : ',round(circumference_circle, 2))