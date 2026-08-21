# other built-in function -- min, max, sum
course = ['history', 'Math', 'Physics', 'CompSci']
nums = [2,5,4,7,2,-3,0,44]

print(min(nums))
print(min(course))

print()

print(max(nums))
print(max(course))

print()

print(sum(nums))
# print(sum(course)) #obvious error dega so, in this case we use join() method
print(' '.join(course))  
print(len(course))

print()



'''
| Function     | Works on          | Example                                               |
| ------------ | ----------------- | ----------------------------------------------------- |
| `sum()`      | Numbers only      | `sum([1,2,3])` → `6`                                  |
| `min()`      | Numbers & Strings | `min(course)` → `'CompSci'` (alphabetically smallest) |
| `max()`      | Numbers & Strings | `max(course)` → `'history'` (alphabetically largest)  |
| `len()`      | Any sequence      | `len(course)` → `4`                                   |
| `' '.join()` | List of strings   | `' '.join(course)`                                    |
'''




