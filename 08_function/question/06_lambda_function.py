# Lambda Function
# Create an anonymous (lambda) function
# that returns the cube of a given number.
# Example:
# cube(2)    -> 8
# cube(3)    -> 27
# cube(5)    -> 125


# ==============================
# What is a Lambda Function?
# ==============================
# A lambda function is a small anonymous function.
# Anonymous means the function is created
# without using the 'def' keyword.
# Lambda functions are useful when you need
# a simple function for a short period of time.


# ==============================
# Normal Function
# ==============================
# Instead of writing:

def cube(num):
    return num ** 3

print(cube(3))    # 27


print()


# ==============================
# Lambda Function
# ==============================
# We can write the same function
# using the lambda keyword.

cube = lambda num: num ** 3

print(cube(3))    # 27
print(cube(5))    # 125


print()


# ==============================
# Syntax
# ==============================
#
# function_name = lambda parameters: expression
#
# Example:
#
# square = lambda x: x ** 2
# add = lambda a, b: a + b
# is_even = lambda x: x % 2 == 0


# Example 1
square = lambda x: x ** 2
print(square(4))


# Example 2
add = lambda a, b: a + b
print(add(10, 20))


# Example 3
is_even = lambda x: x % 2 == 0
print(is_even(8))
print(is_even(5))


'''
Difference Between def and lambda

Normal Function (def)

- Uses the def keyword.
- Can contain multiple statements.
- Can have loops and if-else.
- Requires the return keyword.

Lambda Function

- Uses the lambda keyword.
- Contains only one expression.
- Automatically returns the result.
- Best for short and simple functions.
'''


'''
When Should You Use Lambda?

Use lambda when:

- The function is very small.
- It is used only once.
- You want cleaner code.
- It is passed to functions like
  map(), filter(), and sorted().

Avoid lambda when:

- The logic is complex.
- Multiple statements are needed.
- Readability becomes poor.

In these cases, use a normal function.
'''


'''
Interview Note

A lambda function:

- is an anonymous function.
- can have any number of parameters.
- contains only one expression.
- automatically returns the result
  of that expression.
- cannot contain multiple statements.
- is commonly used with:
    • map()
    • filter()
    • sorted()
'''


print()
# with multiple parameter
addition = lambda a , b, c: a +b+c
print(addition(2,3,4))