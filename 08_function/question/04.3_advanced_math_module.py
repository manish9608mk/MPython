# Advanced Math Module

import math


# ==========================================================
# 1. Integer Square Root
# ==========================================================

'''
math.isqrt()

Returns the integer square root of a non-negative integer.

Unlike math.sqrt(), it returns an integer.

Syntax:
math.isqrt(number)
'''

print("========== INTEGER SQUARE ROOT ==========")

print(math.isqrt(25))
print(math.isqrt(26))
print(math.isqrt(50))

print()


# ==========================================================
# 2. Combination (nCr)
# ==========================================================

'''
math.comb()

Returns the number of combinations.

Formula:

n!
---------
r!(n-r)!

Syntax:

math.comb(n, r)
'''

print("========== COMBINATION ==========")

print(math.comb(5, 2))
print(math.comb(10, 3))

print()


# ==========================================================
# 3. Permutation (nPr)
# ==========================================================

'''
math.perm()

Returns the number of permutations.

Formula:

n!
---------
(n-r)!

Syntax:

math.perm(n, r)
'''

print("========== PERMUTATION ==========")

print(math.perm(5, 2))
print(math.perm(10, 3))

print()


# ==========================================================
# 4. Product
# ==========================================================

'''
math.prod()

Returns the product of all elements in an iterable.

Syntax:

math.prod(iterable)
'''

print("========== PRODUCT ==========")

numbers = [2, 3, 4, 5]

print(math.prod(numbers))

print()


# ==========================================================
# 5. Distance Between Two Points
# ==========================================================

'''
math.dist()

Returns the Euclidean distance between two points.

Syntax:

math.dist(point1, point2)
'''

print("========== DISTANCE ==========")

point1 = (1, 2)
point2 = (4, 6)

print(math.dist(point1, point2))

print()


# ==========================================================
# 6. Hypotenuse
# ==========================================================

'''
math.hypot()

Returns the length of the hypotenuse.

Formula:

√(x² + y²)
'''

print("========== HYPOT ==========")

print(math.hypot(3, 4))

print()


# ==========================================================
# 7. Degrees to Radians
# ==========================================================

'''
math.radians()

Converts degrees into radians.
'''

print("========== RADIANS ==========")

print(math.radians(180))

print()


# ==========================================================
# 8. Radians to Degrees
# ==========================================================

'''
math.degrees()

Converts radians into degrees.
'''

print("========== DEGREES ==========")

print(math.degrees(math.pi))

print()


# ==========================================================
# 9. Truncate
# ==========================================================

'''
math.trunc()

Removes the decimal part.

Does not round.
'''

print("========== TRUNC ==========")

print(math.trunc(4.9))
print(math.trunc(-4.9))

print()


# ==========================================================
# 10. Modf
# ==========================================================

'''
math.modf()

Returns the fractional part and integer part
as a tuple.
'''

print("========== MODF ==========")

fractional, integer = math.modf(12.75)

print(fractional)
print(integer)

print()


# ==========================================================
# 11. Copy Sign
# ==========================================================

'''
math.copysign()

Returns a float with the magnitude of x
and the sign of y.
'''

print("========== COPYSIGN ==========")

print(math.copysign(10, -2))
print(math.copysign(-10, 2))

print()


# ==========================================================
# 12. Finite / Infinite / NaN
# ==========================================================

'''
Useful while working with floating-point numbers.
'''

print("========== FINITE ==========")

print(math.isfinite(10))
print(math.isfinite(float("inf")))
print(math.isfinite(float("nan")))

print()

print("========== INFINITE ==========")

print(math.isinf(float("inf")))
print(math.isinf(100))

print()

print("========== NAN ==========")

print(math.isnan(float("nan")))
print(math.isnan(10))

print()


# ==========================================================
# Interview Notes
# ==========================================================

'''
Frequently Asked in DSA

★★★★★

math.isqrt()
math.gcd()
math.lcm()

★★★★☆

math.comb()
math.perm()

★★★☆☆

math.prod()
math.dist()
math.hypot()

★★☆☆☆

math.modf()
math.trunc()
math.copysign()

★

math.isfinite()
math.isinf()
math.isnan()

Remember:

math.sqrt()

↓

Returns float


math.isqrt()

↓

Returns integer
'''


print('============ DIR MATH ==========')
print(dir(math))