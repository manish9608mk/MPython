# tuples are very similar to list but with one major difference so, we can't modify tuples
# so, in programming this is called as mutable and immutable 
# so, list are mutable and tuples are not they are immutable
# in tuples instead of using [] or square bracket we use this () or parenthesis bracket 


print()
# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)




print()
# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art' 
# # and here, now if we add new item at index 0, it gives TypeError: 'tuple' object does not support item assignment, thats why it is immutable, but we see above we are able to add new items in list 

# print(tuple_1)
# print(tuple_2)



print()
# Tuples have only two useful methods -- count() , index()
'''
Easy Rule to Remember
index(value) → "Ye value kis index par hai?"
tuple[index] → "Is index par kaunsi value hai?"
'''
t =(3,6,2,8,4,0,4,4,4,)
print(t.count(4))  # 4
print(t.count(3))  # 1
print()
print(t[4])   # 4
print(t[0])   # 3
print(t.index(3))  # 0
print(t.index(8))  # 3
print(t.index(4))  # 4 (first occurrence)
print(t.index(0))  # 5



print()
# Can a tuple contain a list? -- YES
data = (1, 2, [3, 4])
data[2].append(5)
print(data)



'''
List vs Tuple in Python

| Feature            | List                        | Tuple             |
| ------------------ | --------------------------- | ----------------- |
| Syntax             | `[]`                        | `()`              |
| Mutable?           | ✅ Yes                       | ❌ No              |
| Can add items?     | ✅ Yes (`append()`)          | ❌ No              |
| Can remove items?  | ✅ Yes (`remove()`, `pop()`) | ❌ No              |
| Can modify items?  | ✅ Yes                       | ❌ No              |
| Ordered?           | ✅ Yes                       | ✅ Yes             |
| Allows duplicates? | ✅ Yes                       | ✅ Yes             |
| Faster             | ❌ Slightly slower           | ✅ Slightly faster |
| Memory usage       | More                        | Less              |
| Best for           | Data that changes           | Fixed data        |

'''


'''
Lists have many methods:
append()
extend()
insert()
remove()
pop()
sort()
reverse()
clear() etc.

but, Tuples have only two useful methods.
count()
index()

'''






'''
REVISION

1. Python Built-ins: Learn every one.

len()
sum()
max()
min()
sorted()
list.sort()
range()
enumerate()
zip()
map()
filter()
set()
dict()
Counter()
defaultdict()
deque()
heapq()
bisect()



Learn these methods
LIST

append()
pop()
extend()
insert()
remove()
reverse()
sort()


DICTIONARY

get()
items()
keys()
values()
update()


SET

add()
remove()
discard()
union()
intersection()

'''