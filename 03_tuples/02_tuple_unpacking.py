# Tuple Unpacking / List Unpacking (Sequence Unpacking)
# Sequence unpacking works with tuples, lists, and other iterable objects.

'''
Tuple Unpacking:
Tuple unpacking is the process of assigning each value of a tuple
to separate variables in a single statement.

Syntax:
variable1, variable2, ... = tuple_object

The number of variables and tuple values must be the same.

For Interview: 
Tuple Unpacking is the process of assigning multiple values from a tuple to multiple variables in a single statement.
'''

# Example 1

person = ("Mani", 21)

# Normally (Using Indexing)
print(person[0])      # Mani
print(person[1])      # 21

print()

# Using Tuple Unpacking
name, age = person

print(name)           # Mani
print(age)            # 21


'''
How does Tuple Unpacking work?

person = ("Mani", 21)
↓
name, age = person

Python internally does:
name = person[0]
age  = person[1]
↓
name = "Mani"
age  = 21
'''


print()
# Another Example

student = ("Rahul", 20, "Bhopal")
name, age, city = student

print(name)
print(age)
print(city)



print()
# Function Returning Multiple Values

def get_data():
  # Returns a tuple
  return "Steve", 23

name, age = get_data()

print(name)
print(age)


'''
Why is Tuple Unpacking useful?

1. Cleaner code
2. Easy to read
3. No need to access values using indexes.
4. Commonly used when a function returns multiple values.
'''


'''
Rules of Tuple Unpacking

✔ Number of variables must match the number of tuple values.

Correct:

person = ("Mani", 21)
name, age = person

Incorrect:

person = ("Mani", 21)
name = person          # name becomes the whole tuple

name, age, city = person

ValueError:
not enough values to unpack
(expected 3, got 2)

Another Incorrect Example:

student = ("Rahul", 20, "Bhopal")

name, age = student

ValueError:
too many values to unpack
(expected 2)


✔ Order matters.

person = ("Mani", 21)
name, age = person

name → "Mani"
age  → 21

If the order changes:
age, name = person

age  → "Mani"
name → 21
This results in incorrect variable assignments.


✔ Tuple unpacking also works with lists.

student = ["Rahul", 20]
name, age = student
'''


'''
Easy Memory Trick

Tuple

("Mani", 21)

↓

Tuple Unpacking

name, age = person

↓

Python automatically does

name = "Mani"
age = 21
'''


'''
Real-World Example

Imagine a student record.

student = ("Rahul", 20)

Instead of writing

student[0]
student[1]

You can directly write

name, age = student

Now,

name → Rahul
age  → 20

This makes the code cleaner and easier to understand.
'''




'''
Unpacking works only with iterable objects whose number of elements matches the number of variables.

| Object     | Iterable |      Unpacking Works?     | Example                 |
| ---------- | :------: | :-----------------------: | ----------------------- |
| List       |     ✅    |             ✅             | `a, b = [10, 20]`       |
| Tuple      |     ✅    |             ✅             | `a, b = (10, 20)`       |
| String     |     ✅    |             ✅             | `a, b, c = "CAT"`       |
| Dictionary |     ✅    | ✅ (Keys unpack hote hain) | `a, b = {"x":1, "y":2}` |
| Set        |     ✅    |  ✅ (Order not guaranteed) | `a, b = {10, 20}`       |
| Range      |     ✅    |             ✅             | `a, b, c = range(3)`    |

'''