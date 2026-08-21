# Recursive Function

# Create a recursive function that calculates
# the factorial of a given number.

# A recursive function is a function
# that calls itself until a base case is reached.

# Example:
# factorial(5)
# -> 5 × 4 × 3 × 2 × 1 -> 120
# factorial(4) -> 24
# factorial(1) -> 1



# Approach 1: Iterative (Forward Loop)
def factorial(n):
    result = 1

    # Loop from 1 to n
    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))



print()
# Approach 2: Iterative (Backward Loop)
def factorial(n):
    result = 1

    # Loop from n to 1
    for i in range(n, 0, -1):
        result *= i

    return result

print(factorial(5))



print()
# Approach 3: Recursive Approach
def factorial(n):

    # Base Case (Stop Condition)
    if n == 0:
        return 1

    # Recursive Case
    # n! = n × (n-1)!
    return n * factorial(n - 1)

print(factorial(5))



print()
# Approach 4: Built-in Function
# Uses Python's built-in math.factorial()
# to calculate the factorial directly.
import math

print(math.factorial(5))



print()
# Approach 5: Generator
# Generates the factorial value at each step.
# Useful for understanding how the factorial
# is built step by step.

def factorial_steps(n):
    result = 1

    for i in range(1, n + 1):
        result *= i
        yield result

for step in factorial_steps(5):
    print(step)



print()
# Approach 6: While Loop
# Uses a while loop instead of a for loop.
def factorial(n):
    result = 1

    while n > 0:
        result *= n
        n -= 1

    return result

print(factorial(5))