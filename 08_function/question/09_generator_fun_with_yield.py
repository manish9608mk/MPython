# Generator Function with yield

# Create a generator function using the
# yield keyword that generates even numbers
# up to a specified limit.

# Example:
# even_numbers(10)
# -> 2
# -> 4
# -> 6
# -> 8
# -> 10


# Method 1: Loop
for num in range(1,11):
   if num % 2 == 0:
      print('Even: ', num)
# Even:  2
# Even:  4
# Even:  6
# Even:  8
# Even:  10



print()
# Method 2: List + return 
def even_number(limit):
    even = []

    for i in range(1, limit + 1):
        if i % 2 == 0:
            even.append(i)

    return even

print(even_number(10)) # [2, 4, 6, 8, 10] 




print()
# Method 3: Function + print 
def even_number(limit):
   for i in range(1, limit+1):
      if i % 2 == 0:
         print(i)     

even_number(10)
# 2
# 4
# 6
# 8
# 10



print()
# Method 4: return i 
def even_number(limit):
   for i in range(1, limit+1):
      if i % 2 == 0:
         return i      

print(even_number(10)) # 2 




print()
# Method 5: Generator Function (finally)
def even_number(limit):
   for i in range(1, limit+1):
      if i % 2 == 0:
         yield i 

# generator function         
for num in even_number(10):
    print(num)

print(even_number(10)) 




print()
# Method 5: Generator Function with detailed comments

def even_number(limit):
    for i in range(1, limit + 1):
        if i % 2 == 0:
            yield i

# A generator does NOT print values directly.
# It returns a generator object.

print(even_number(10))
# Output:
# <generator object even_number at 0x...>

# To get the generated values,
# iterate over the generator.

for num in even_number(10):
    print(num)

# Output:
# 2
# 4
# 6
# 8
# 10


'''
Diagram:
print()
↓
Display
----------------------
return
↓
Final Result
↓
STOP
----------------------
yield
↓
Next Value
↓
PAUSE
↓
Continue Later



| `return`          | `yield`                    |
| ----------------- | -------------------------- |
| Ends the function | Pauses the function        |
| Returns once      | Can produce many values    |
| Cannot resume     | Resumes from the same line |
| Normal function   | Generator function         |



return
↓
Ends the function immediately.
-------------------------
yield
↓
Produces one value,
Temporarily pauses the function while remembering its current state,
and resumes from the same point later.



- yield is a keyword used to create a generator function.
It produces one value at a time, temporarily pauses the function,
and resumes execution from the same point when the next value is requested.
- A Generator Function is a special type of function that uses the yield keyword instead of return to produce values one at a time.



|       Situation                                    |        Use        |
| -------------------------------------------------- | ----------------- |
| You only want to display the output                | `print()`         |
| You need to use the result later in your program   | `return`          |
| You need the first matching value only             | `return`          |
| You need all values together at once               | `return` + `list` |
| You are working with a very large sequence of data | `yield`           |
| You need to produce values one at a time           | `yield`           |



How Python Thinks:
For yield lifecycle -

Function starts
↓
yield value
↓
Pause
↓
Next requested?
↓
Continue after yield
↓
yield next value
↓
Pause
↓
Repeat
↓
Function ends


Generator Lifecycle -

Generator Function
↓
Generator Object
↓
for loop / next()
↓
One value generated
↓
Pause
↓
Next value requested
↓
Continue



Interview Question
Q. Why not use return instead of yield?
Answer:
Because return ends the function after one result,
whereas yield allows the function to produce
multiple values one at a time without storing
them all in memory.



Lazy Evaluation -
Generators create values only when they are requested.
They do not generate all values in advance,
which makes them memory efficient.
'''




# Example 6: Using next()
print()
# next() is a built-in function that asks a generator (or any iterator) to produce its next value.


def even_number(limit):
    for i in range(1, limit + 1):
        if i % 2 == 0:
            yield i

g = even_number(10)   # Generator Object

print(next(g))   # 2
print(next(g))   # 4
print(next(g))   # 6
print(next(g))   # 8
print(next(g))   # 10

'''
Generator Function
        │
        ▼
Generator Object
        │
        ├── for loop  → Calls next() automatically ✅
        │
        └── next()    → You call it manually ✅
'''
