# Default Parameter Value
# Create a function that greets a user.
# If no name is provided, the function should
# greet the user with a default name.
#
# Example:
# greet()          -> Hello, Guest!
# greet("Mani")    -> Hello, Mani!


# Example 1 - Basic Approach
# Returns only the user's name.
# It demonstrates the use of a default parameter,
# but it does not return a greeting message.
def greet(name='Guest'):
    return name

print("Hello", greet())
print("Hello", greet("Mani!"))



print()
# Example 2 - Correct Approach (Recommended)
# This function returns a complete greeting message.
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())
print(greet("Mani"))



print()
# Example 3 - Using print() inside the function
# This approach directly prints the greeting
# instead of returning it.
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Mani")



'''
Note:

Example 1 and Example 2 return a value.

Since they return a value, they can be reused
in other functions, files, or programs.

Example 3 only prints the output.

Since it does not return a value, its result
cannot be directly reused in another function
or assigned to a variable.

Therefore, returning a value is generally
preferred over printing inside a function.
'''


'''
Interview Note:

Prefer returning values from a function instead of
printing them inside the function.

A function that returns a value is more reusable,
testable, and flexible.
'''




print()
# Multiple Default Parameters
def introduce(name="Guest", age=18):
    return f"{name} is {age} years old."

print(introduce())
print(introduce("Mani"))
print(introduce("Mani", 22))


print()
# Mutable Default Arguments important for interview
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

# problem
print(add_item(1)) # [1]        expected [1]
print(add_item(2)) # [1, 2]     expected [2]
# Ye Python ka famous Mutable Default Argument Pitfall hai.

# correct way
print()
def add_item(item, my_list=None):

    if my_list is None:
        my_list = []

    my_list.append(item)

    return my_list

print(add_item(1))
print(add_item(2))