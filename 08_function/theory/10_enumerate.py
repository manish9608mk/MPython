# enumerate
# enumerate() is a built-in Python function used when you want to iterate over a sequence and get both the index and the value at the same time.
# enumerate() does not make the algorithm faster.

# ex1 - without enumerate()
fruits = ['apple', 'banana', 'mango']
for i in range (len(fruits)):
  print(i, fruits[i])

'''
o/p
0 apple
1 banana
2 mango
'''

print()
# ex2 - with enumerate()
fruits = ['apple','banana', 'mango']
for i, fruit in enumerate(fruits):
  print(i, fruit)

'''
o/p
0 apple
1 banana
2 mango

It's cleaner and more Pythonic.

How enumerate() works:
Conceptually:

enumerate(["apple", "banana", "mango"])

produces pairs like:
(0, "apple")
(1, "banana")
(2, "mango")

So:
for index, fruit in enumerate(fruits):

means:
index → 0, 1, 2
fruit → apple, banana, mango

enumerate() returns an iterator of (index, value) pairs.
fruits = ['apple', 'banana', 'mango']
print(list(enumerate(fruits)))
Output:
[(0, 'apple'), (1, 'banana'), (2, 'mango')]
You don't need to memorize the implementation. Just understand the behavior.
'''


print()
# ex3
# Starting index from something else
# By default, indexing starts at 0.
# we can change it using start:
fruits = ['apple', 'banana', 'mango']
for i, fruit in enumerate (fruits , start=1):
  print(i,fruit)

'''
o/p
1 apple
2 banana
3 mango


Syntax:
enumerate(iterable, start=0)
- iterable → list, tuple, string, etc.
- start → starting index
- default start = 0
'''


print()
# ex4 - With a string
word = ('mango')
for index, char in enumerate(word):
  print(index, char)


print()
# ex5
# Very useful in DSA
# suppose list is given and You want to find the index of 30 or any number:
nums =[45,23,56,78,67,30,56,78,90]
for i, num in enumerate(nums):
  if num == 30:
    print('found at index:',i)    # 5

'''
This is very common in array/string problems.

Interview tip - 
Whenever you think:

I need both index and element while traversing.

Think:

for i, value in enumerate(arr):

instead of:

for i in range(len(arr)):
    value = arr[i]

Both work, but enumerate() is generally cleaner and more Pythonic.



Where is it useful in DSA?
1. Finding an element's index
2. Comparing current element with something
3. Updating another array using the index
4. String problems - Very useful because strings have indexes.
5. Two arrays


DSA Algorithm
     ↓
Array traversal
     ↓
Need index + value?
     ↓
Use enumerate()

enumerate() doesn't magically improve Big-O. It mainly improves code readability and reduces indexing mistakes.


Complexity:
Time Complexity: O(n)
Extra Space: O(1) when directly iterating with enumerate()


DSA mental model:
Need only values?
        ↓
for value in arr:

Need index + value?
        ↓
for i, value in enumerate(arr):

Need custom starting index?
        ↓
enumerate(arr, start=1)

'''
