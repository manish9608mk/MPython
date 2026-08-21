# Function with *args
# Create a function that accepts a variable
# number of positional arguments using *args
# and returns their sum.
# Example:
# add(1, 2)            -> 3
# add(1, 2, 3)         -> 6
# add(10, 20, 30, 40)  -> 100

# ex1 - with built-in sum() function
def sum_all(*args):
  return sum(args)  # sum inbuilt function

print(sum_all(1,2))
print(sum_all(1,2,2))
print(sum_all(1,2,2,5))

# ex2 -
print()

def add_all(*args):
  print(args)

  for i in args:
    print(i * 4)
  return sum(args)

print(add_all(1,2,3))


# ex3 - without using the built-in sum() function
print()

def add_all(*args):

    total = 0

    print(args)   # args is a tuple

    for num in args:
        total += num

    return total

print(add_all(1, 2, 3)) # 6
print(add_all(10, 20, 30, 40)) # 100