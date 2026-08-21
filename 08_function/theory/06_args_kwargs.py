# *args → Variable number of positional arguments. or, unknown number of positional arguments (tuple)
# **kwargs → Variable number of keyword arguments. or, unknown number of keyword arguments (dictionary)
# args and kwargs are conventions or just a name, not keywords.
# The * and ** are important, not the names.
# *args creates a tuple.
# **kwargs creates a dictionary.


# Example 1 : *args
def add(*numbers):
  print(numbers)

add(2)
add(2,3)
add(2,3,4,5)
add(9,4)
# output
# (2,)
# (2, 3)
# (2, 3, 4, 5)
# (9, 4)
# notice: numbers is a tuple.



print()
# Example 2 : *args
def add(*numbers):
  total = 0

  for num in numbers:
    total += num

  print(total)

add(2,3)
add(20,30,5)  
add(1,2,3,4,5)  
  

# Example 3 : **kwargs
# **kwargs : Suppose we don't know how many keyword arguments the user will send.
print()

def student(**details):

    print(details)

student(
    name="Rahul",
    age=21,
    city="Delhi"
)

# Output: {'name': 'Rahul', 'age': 21, 'city': 'Delhi'}
# Notice: output details is a dictionary.



# Example 4 : **kwargs
print()

def student(**details):

    for key, value in details.items():
        print(key, ":", value)

student(
    name="Rahul", age=21, city="Delhi"
)


'''
Golden Rule:
| *args            | **kwargs              |
| ---------------- | -------------------   |
| Many values      | Many **named** values |
| Tuple            | Dictionary            |
| Position matters | Name matters          |

'''



# Mixed example
print()

def show(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

show(10, 20, 30, name="Steve", age=22)





'''
Rule to Remember:

Normal Parameters
↓
Use when you know exactly how many arguments are needed.

*args
↓
Use when you don't know how many positional arguments will come.

**kwargs
↓
Use when you don't know how many keyword arguments will come.
'''