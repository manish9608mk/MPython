'''
Common Set Methods

| Method       | Purpose                              |
| ------------ | ------------------------------------ |
| `add(x)`     | Add an element                       |
| `remove(x)`  | Remove an element (error if missing) |
| `discard(x)` | Remove safely (no error if missing)  |
| `pop()`      | Remove a random element              |
| `clear()`    | Remove all elements                  |
| `copy()`     | Make a copy                          |
   etc.
'''

#Example1
num = {3,4,6,3,7,9,4,6,2,22}

print(num)

num.add(0)
print(num)

num.remove(4)
print(num)

num.discard(22)
print(num)

num.copy()
print(num)

num.clear()
print(num)


# print(num[10])
#TypeError: 'set' object is not subscriptable -- Because sets have no fixed order, there is no index 0, 1, etc.



print()
#Example2
fruits = {"apple","banana",'mango','Orange'}

print(fruits)

fruits.add("Kiwi")
print(fruits)

fruits.remove("Orange")
print(fruits)