# KEYWORD ARGUMENTS IN PYTHON

# Keyword arguments allow us to pass arguments
# using the parameter names.
# This makes the function call more readable.

# Example 1 : Positional Arguments
# Normally we call a function like this:
def introduce(name, age):
  print("Name: ", name)
  print("Age: ", age)

introduce('manish', 20)  
introduce(20, 'manish')


# Example 2 : Keyword Arguments
# Now use the parameter names.
print()

def introduce(name, age):
    print("Name:", name)
    print("Age:", age)

introduce(age=22, name="Steve")
# Notice something?
# We changed the order.
# Still the output is correct because Python matches by parameter name, not position.


# Example 3 : Keyword Arguments
print()
def student(name, age, city):
    print(name)
    print(age)
    print(city)

student(city="Delhi", age=21, name="Rahul")



# Example 4 : Mixing Positional and Keyword Arguments
print()
def introduce(name, age):
    print("Name:", name)
    print("Age:", age)

introduce("Steve", age=22)

# Rule:
# Positional arguments must come before keyword arguments.

# ✔ Correct
# introduce("Steve", age=22)

# ❌ Wrong
# introduce(name="Steve", 22)
# SyntaxError: positional argument follows keyword argument