'''
Math Module: 

1. Introduction
2. Importing math module
3. Constants
   • math.pi
   • math.e

4. Rounding Functions
   • round()
   • math.ceil()
   • math.floor()

5. Mathematical Functions
   • math.sqrt()
   • math.pow()
   • abs()
   • math.fabs()

6. Number Theory (Very Important for DSA)
   • math.gcd()
   • math.lcm()
   • math.factorial()

7. Logarithmic Functions
   • math.log()
   • math.log10()

8. Trigonometric Functions
   • math.sin()
   • math.cos()
   • math.tan()

9. Precision Formatting
   • f"{num:.2f}"
   • round()

10. Real-world Examples

11. Interview Notes
'''


# Math Module

'''
Math Module

The math module provides mathematical functions and constants
that are commonly used in Python programs.

Before using the math module, we need to import it.

Syntax:
import math
'''

import math


# ==========================================================
# 1. Constants
# ==========================================================

'''
Math Constants

math.pi
Represents the value of π (Pi).

math.e
Represents Euler's Number.
'''

print("========== CONSTANTS ==========")

print("Value of PI:", math.pi)
print("Value of e :", math.e)

print()


# ==========================================================
# 2. Square Root
# ==========================================================

'''
math.sqrt()

Returns the square root of a number.

Syntax:
math.sqrt(number)
'''

print("========== SQUARE ROOT ==========")

print(math.sqrt(25))
print(math.sqrt(64))
print(math.sqrt(100))

print()


# ==========================================================
# 3. Power
# ==========================================================

'''
math.pow()

Raises a number to a given power.

Syntax:
math.pow(base, exponent)

Note:
Normally we use ** operator because it is more common in Python.
'''

print("========== POWER ==========")

print(math.pow(2, 3))
print(math.pow(5, 2))

print()

print(2 ** 3)
print(5 ** 2)

print()


# ==========================================================
# 4. Ceiling
# ==========================================================

'''
math.ceil()

Rounds a number UP to the nearest integer.
'''

print("========== CEIL ==========")

print(math.ceil(4.2))
print(math.ceil(4.8))
print(math.ceil(5.0))

print()


# ==========================================================
# 5. Floor
# ==========================================================

'''
math.floor()

Rounds a number DOWN to the nearest integer.
'''

print("========== FLOOR ==========")

print(math.floor(4.2))
print(math.floor(4.8))
print(math.floor(5.0))

print()


# ==========================================================
# 6. Round
# ==========================================================

'''
round()

Rounds a number to the specified number of digits.

Syntax:
round(number, digits)
'''

print("========== ROUND ==========")

pi = math.pi

print(round(pi, 2))
print(round(pi, 3))
print(round(pi, 4))

print()


# ==========================================================
# 7. Precision Formatting
# ==========================================================

'''
Precision Formatting

Using f-strings

Syntax:
f"{number:.2f}"

.2f

.
Decimal point

2
Number of digits after decimal

f
Floating point number
'''

print("========== PRECISION ==========")

print(f"{math.pi:.2f}")
print(f"{math.pi:.3f}")
print(f"{math.pi:.4f}")

print()


# ==========================================================
# 8. Absolute Value
# ==========================================================

'''
abs()

Returns the absolute value of a number.
'''

print("========== ABSOLUTE VALUE ==========")

print(abs(-20))
print(abs(20))
print(abs(-45.6))

print()


# ==========================================================
# 9. Factorial
# ==========================================================

'''
math.factorial()

Returns the factorial of a positive integer.

5! = 5 x 4 x 3 x 2 x 1 = 120
'''

print("========== FACTORIAL ==========")

print(math.factorial(5))
print(math.factorial(6))

print()


# ==========================================================
# 10. Greatest Common Divisor (GCD)
# ==========================================================

'''
math.gcd()

Returns the Greatest Common Divisor.

Very Important for DSA.
'''

print("========== GCD ==========")

print(math.gcd(24, 36))
print(math.gcd(18, 30))

print()


# ==========================================================
# 11. Least Common Multiple (LCM)
# ==========================================================

'''
math.lcm()

Returns the Least Common Multiple.

Available in Python 3.9+
'''

print("========== LCM ==========")

print(math.lcm(6, 8))
print(math.lcm(12, 18))

print()


# ==========================================================
# 12. Logarithm
# ==========================================================

'''
math.log()

Returns the natural logarithm.

math.log10()

Returns logarithm with base 10.
'''

print("========== LOG ==========")

print(math.log(10))
print(math.log10(100))

print()


# ==========================================================
# 13. Trigonometric Functions
# ==========================================================

'''
Trigonometric Functions

math.sin()
math.cos()
math.tan()

Angles are in radians.
'''

print("========== TRIGONOMETRY ==========")

print(math.sin(math.pi / 2))
print(math.cos(0))
print(math.tan(math.pi / 4))

print()


# ==========================================================
# Real-World Example
# ==========================================================

'''
Real-World Example

Calculate the area and circumference
of a circle using math.pi.
'''

print("========== REAL WORLD EXAMPLE ==========")

radius = 4

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")

print()


# ==========================================================
# Interview Notes
# ==========================================================

'''
Interview Notes

Must Know:

✔ math.pi
✔ math.sqrt()
✔ round()
✔ math.ceil()
✔ math.floor()
✔ math.factorial()
✔ math.gcd()
✔ math.lcm()
✔ abs()
✔ f"{number:.2f}"

Good to Know:

✔ math.e
✔ math.pow()
✔ math.log()
✔ math.log10()

Basic Knowledge:

✔ math.sin()
✔ math.cos()
✔ math.tan()

Remember:

math.pow(2,3)

and

2 ** 3

give the same mathematical result.

Python programmers generally prefer

2 ** 3

because it is shorter and more Pythonic.
'''