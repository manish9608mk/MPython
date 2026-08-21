# choose when to use 
# Python has 2 types of loops: for loop , while loop
# Iteration = Loop ka ek chakkar

'''
Interview Points
- Use a for loop when you know the number of iterations.
- Use a while loop when you don't know how many times the loop will run (e.g., user input, waiting for a condition, reading data until the end).
'''

# 1. for loop
# A for loop is used to iterate over a sequence like a list, string, tuple, set, dictionary, or range().

'''
FOR LOOP

for variable in sequence:
    # Work to do


OR 

for i in range(start, stop, step):
    # Work to do
'''





# 2. while loop
# A while loop executes as long as a condition is True.

'''
WHILE LOOP

count = 1      # Initialization

while count <= 5:    # Condition
    print(count)     # Loop body
    count += 1       # Update

    
A while loop has 3 important parts:
- Initialization → Start value
- Condition → When to stop
- Update → Change the value each iteration    
'''

# Loop Control Statements
# break-(Stops the loop immediately.) 
# continue-(Skips the current iteration.) 
# pass-(Placeholder that does nothing. Useful while writing incomplete code.)


print()
# else with Loops 
# The else block runs if the loop finishes normally (without break)
for i in range(3):
    print(i)
else:
    print("Loop completed")


print()
# Nested Loops : A loop inside another loop.
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)




print()
# Common Functions Used with Loops

# range()
for i in range(5):
    print(i)

# enumerate()
print()
name = "pyenumerate"

for index, char in enumerate(name):
    print(index, char)

# zip()
print()
names = ["zip", "zip2"]
marks = [90, 85]

for name, mark in zip(names, marks):
    print(name, mark)      

# reversed()
print()
for i in reversed(range(5)):
    print(i)




'''
| Loop Type          | Complexity |
| ------------------ | ---------- |
| Single loop        | O(n)   |
| Nested loop        | O(n²)  |
| Triple nested loop | O(n³)  |



When Companies Use Loops
- for Loop
Traversing arrays/lists
Processing strings
Reading files line by line
Iterating over database records
API response processing



- while Loop
Waiting for user input
Retry mechanisms
Game loops
Network communication
Background services



Understanding range()
range(start, stop, step)
Parameters:
start → Included
stop → Excluded
step → Increment/Decrement



Loops
│
├── for
├── while
│
├── range()
│   ├── start
│   ├── stop
│   └── step
│
├── Dry Run
│
├── break
├── continue
├── pass
├── else
│
├── Patterns
│   ├── Traversal
│   ├── Accumulator
│   ├── Counter
│   ├── Flag
│   ├── Transformation
│   └── Simulation
│
└── Complexity
    ├── O(n)
    └── O(n²)
'''