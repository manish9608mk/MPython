# Example 1: Using List
# - Store all numbers (1 to 100) inside a list.
# - The entire list is created in memory.
# - This approach is simple but uses more memory.

import sys  # Used to measure the memory size of an object.

def create_list():
    
    numbers = []
    i = 1
    while i <= 100:
        numbers.append(i)
        i += 1
    return numbers

numbers = create_list()
print(numbers)

# Size of the list object in memory.
print(sys.getsizeof(numbers))

# Create a new list by adding 10 to every element.
print([num + 10 for num in numbers])





print()
# Example 2: Using range()
# range() generates numbers efficiently. Converting it into a list stores all numbers in memory. 
numbers = list(range(1,101))
print(numbers)




print()
# Example 3: Generator (yield) 
# A generator does not store all values. It produces one value at a time.
# This makes generators memory efficient, especially for very large sequences.
def create_generator():
    i = 1
    while i <= 100:
        yield i
        i += 1

# Returns a generator object.
print(create_generator())

# Create a generator object.
x = create_generator()

# Get values one by one.
print(next(x))
print(next(x))
print(next(x))

# Convert the remaining generated values into a list
# The generator continues from where it last paused.
print(list(x))


'''
Q. Why are generators memory efficient?
Answer:
Generators do not store all values in memory.
They generate one value at a time using the
yield keyword and pause after each value.

When the next value is requested, execution
continues from where it previously stopped.

This makes generators ideal for working
with very large datasets.


One-line Revision

List
↓
Stores all values in memory.

Generator
↓
Generates one value at a time.

yield
↓
Generate → Pause → Resume

'''