# Set is an unordered collection of unique elements.
#Set is a built-in data structure in Python that stores a collection of unique elements.

'''
List vs Tuple vs Set

| Feature      | List | Tuple | Set          |
| ------------ | ---- | ----- | ------------ |
| Syntax       | `[]` | `()`  | `{}`         |
| Ordered      | ✅    | ✅     | ❌            |
| Mutable      | ✅    | ❌     | ✅            |
| Duplicates   | ✅    | ✅     | ❌            |
| Indexing     | ✅    | ✅     | ❌            |
| Hash Table   | ❌    | ❌     | ✅            |
| Search Speed | O(n) | O(n)  | O(1) average |

'''


# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Biology','Math'}
art_courses = {'History', 'Math', 'Art', 'CompSci', 'Design'}

print(cs_courses)
print('Biology' in cs_courses)


print()
# intersection() method -- it tells common item 
print(cs_courses.intersection(art_courses)) 

# but when i want to know what cources in the cs_cources but not in art_cources, then we use -- difference() method
print(cs_courses.difference(art_courses))

#when i have to combine all offered courses then we use -- union() method
print(cs_courses.union(art_courses))
