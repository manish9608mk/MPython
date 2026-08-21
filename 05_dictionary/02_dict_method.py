student_1 = {'name':'sonu', 'age': 12, 'city':'begusarai', 'course':['math','Science','english']}
#or
student_2 = dict(name ='saurabh', age =13, state ='Bihar', phone_no = 4819, course=['math','physics','chemistry'] )

print(student_1)
print(student_2)

#accessing
print(student_1['name'])
print(student_1['course'])

# print(student_1['phone']) # gives -- KeyError: 'phone' so, we use get() method
#accessing best way
print(student_1.get('phone'))
print(student_1.get('name'))



print()
# how we can add new entry to the dictionary
student_1['phone'] = '960844583'
print(student_1)

student_1['name'] = 'sonu kumar'   # now sonu becomes sonu kumar 
print(student_1)



print()
# update() method -- we can also update() to update the value 
student_2.update({'name': 'saurabh kumar', 'age': 14})
print(student_2)



print()
# del keyword -- now we want to delete the specific key and its value 
del student_2['age']
print(student_2)
# pop() method -- another way to delete 
student_2.pop('state')
print(student_2)



print()
# finding how many keys in the dictionary 
print(len(student_1))
print(student_1.keys())
print(student_1.values())
print(student_1.items()) # keys and values

print(len(student_2))
print(student_2.keys())
print(student_2.values())
print(student_2.items())



print()
#looping through the keys
for key in student_1:
  print(key)
  
print()
# keys and values using loop
for key,value in student_1.items():
  print(key,value)  





# Dictionary Methods
'''
Dictionary Methods
| Method      | Purpose                   |
| ----------- | ------------------------- |
| `get()`     | Get value safely          |
| `keys()`    | All keys                  |
| `values()`  | All values                |
| `items()`   | Key-value pairs           |
| `pop()`     | Remove one item           |
| `popitem()` | Remove last inserted item |
| `update()`  | Update dictionary         |
| `clear()`   | Remove all items          |
| `copy()`    | Copy dictionary           |

| Method         | Example                         | Output                                  |
| -------------- | ------------------------------- | --------------------------------------- |
| `get()`        | `d.get("name")`                 | Returns value or `None`                 |
| `keys()`       | `d.keys()`                      | `dict_keys([...])`                      |
| `values()`     | `d.values()`                    | `dict_values([...])`                    |
| `items()`      | `d.items()`                     | `dict_items([...])`                     |
| `pop()`        | `d.pop("age")`                  | Removes `"age"` and returns its value   |
| `popitem()`    | `d.popitem()`                   | Removes last inserted `(key, value)`    |
| `update()`     | `d.update({"age": 21})`         | Updates dictionary                      |
| `clear()`      | `d.clear()`                     | `{}`                                    |
| `copy()`       | `d.copy()`                      | Returns a shallow copy                  |
| `setdefault()` | `d.setdefault("city", "Delhi")` | Returns existing value or adds `"city"` |
| `fromkeys()`   | `dict.fromkeys(["a","b"], 0)`   | `{'a': 0, 'b': 0}`                      |

Note: fromkeys() is a class method, so it is called as:
      dict.fromkeys(keys, value)
'''



