# A flag is just a variable that remembers whether something happened or not.
# A flag is a boolean variable (True/False) used to remember
# whether a particular event has happened during program execution.

# Purpose:
# - Track whether something was found.
# - Track whether a condition became true.
# - Make a decision after a loop finishes.

# When to Use:
# ✔ Need a Yes/No answer.
# ✔ Need to remember something after the loop.
# ✔ Need to print a result after searching.

# Time Complexity:
# Depends on the algorithm.
# The flag itself does NOT change time complexity.

numbers = [2, 4, 6, 8, 5]

found = False      # Assume 5 is NOT found

for num in numbers:
    if num == 5:
        found = True    # We found 5
        break

if found:
    print("5 is found.")
else:
    print("5 is not found.")


'''
Visual Memory:

Start
   │
   ▼
flag = False
   │
   ▼
Loop
   │
Condition met?
   │
 ┌─┴─────┐
 │        │
No       Yes
 │        │
 │   flag = True
 │      break
 │
 ▼
Loop Ends
 │
 ▼
Check Flag
 │
 ├── True  → Success
 │
 └── False → Failure
'''