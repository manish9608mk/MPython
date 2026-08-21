# Advanced Default Parameter Concepts

print()

# Multiple Default Parameters
# A function can have more than one default parameter.
# You can override one or all default values by passing arguments.
def introduce(name="Guest", age=18):
    return f"{name} is {age} years old."

print(introduce())
print(introduce("Mani"))
print(introduce("Mani", 22))


print()

# Mutable Default Arguments (Very Important Interview Topic)
# Default mutable objects (like lists, dictionaries, and sets)
# are created only once when the function is defined.
# Therefore, the same object is reused in every function call.
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

# Problem
# Most beginners expect:
#
# add_item(1) -> [1]
# add_item(2) -> [2]
#
# But the actual output is:
#
# add_item(1) -> [1]
# add_item(2) -> [1, 2]
#
# because the same list is reused.

print(add_item(1))
print(add_item(2))


print()

# Correct Approach
# Use None as the default value.
# Create a new list inside the function if no list is provided.
def add_item(item, my_list=None):

    if my_list is None:
        my_list = []

    my_list.append(item)

    return my_list

print(add_item(1))
print(add_item(2))



'''
Interview Note

Avoid using mutable objects such as:

[]
{}
set()

as default parameter values.

Instead, use None and create the mutable object
inside the function.

This avoids unexpected behavior caused by
reusing the same object across multiple function calls.

This is one of the most common Python interview questions.
'''