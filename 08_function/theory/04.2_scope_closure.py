# # LEGB
# x = 100          # Global

# def outer():
#     y = 200      # Enclosing

#     def inner():
#         z = 300  # Local

#         print(z)   # Local
#         print(y)   # Enclosing
#         print(x)   # Global
#         print(len("Hi"))  # Built-in

#     inner()

# outer()




print()
# ✅ Closure
# A Closure is a function that remembers the variables from its enclosing scope even after the enclosing function has finished executing.
# Closure vs Normal Function: 
# | Normal Function                         | Closure                  |
# | --------------------------------------- | ------------------------ |
# | Variables disappear after function ends | Variables are remembered |
# | No saved state                          | Keeps state              |
# | Simple                                  | More powerful            |


def outer():
    x = 10

    def inner():
        print(x)

    return inner

# Create a closure
fun = outer()

# __closure__ returns the variables remembered by the closure.
# Python stores these variables inside special "cell" objects.
print(fun.__closure__)

# outer() returns the inner function object (it does not execute it).
print(outer())

# Access the actual value stored inside the closure.
# Here, the closure remembered x = 10.
print(fun.__closure__[0].cell_contents)
