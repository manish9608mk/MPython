# list comprehension is used for reducing the line of code and......

# ex1 - increment in marks by +2 for bous question
marks = [20,30,40,50,60,70]
new_marks = []
for x in marks:
  new_marks.append(x+2)

print(marks)
print(new_marks)

print()
# # Using List Comprehension
# A shorter and more Pythonic way to create a new list. 
marks = [20,30,40,50,60,70]
new_marks = [x+5 for x in marks]

print(marks)
print(new_marks)




print()
# ex2
cube = []
for x in range(10):
  if x % 2 == 0:
    cube.append(x ** 3)
print('using for loop: ', cube)

# now using list comprehension
cubes_easy = [x ** 3 for x in range(10) if x % 2 == 0]
print('using list comprehension: ', cubes_easy)

'''
cubes_easy = [x ** 3 for x in range(10) if x % 2 == 0]
- Read it like English: 
Store the cube of x for every x in range(10), but only if x is even
- RULE for above comprehension: 
[expression for item in iterable if condition]

Always remember this order.

[
What to Store

for

Where to Iterate

if

Condition
]

'''