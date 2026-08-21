# List Uniqueness Checker
# Check whether all elements in a list are unique.
# If a duplicate element is found, stop the loop and print the duplicate.

'''
Example:

Input:
items = ["apple", "banana", "orange", "apple", "mango"]

Output:
Duplicate found: apple

Explanation:
The second occurrence of "apple" is detected.
The loop stops immediately after finding the first duplicate.
'''

# method 1
items = ["apple", "banana", "orange", "apple", "mango", "mango"]

unique_item = set() # we know it holds always unique item

for item in items:
  if item in unique_item:
    print('Dublicate: ' , item)
    # break
  unique_item.add(item)




# method2 - flag version
print()

items = ["apple", "banana", "orange", "apple", "mango", 'mango']

seen = set()
duplicate_found = False

for item in items:
    if item in seen:
        print(f"Duplicate element found: {item}")
        duplicate_found = True
        break

    seen.add(item)

if not duplicate_found:
    print("All elements are unique.")

'''
Why use a flag?

Without the flag, if there are no duplicates, your program doesn't know what to print after the loop.

The flag remembers what happened inside the loop and lets you make a decision afterward.

This is why the Flag Pattern is so common in programming:

- Assume something (duplicate_found = False).
- Update the flag if a condition occurs.
- After the loop, use the flag to decide what to do.
'''