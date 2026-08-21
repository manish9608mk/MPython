#Syntax

'''
dictionary = {
    key1: value1,
    key2: value2,
    key3: value3
}
'''


# method1
student_1 = {
    "name": "saurabh",
    "age": 20,
    "course": "Math"
}
print(student_1)

# method2 -- Using dict()
student_2 = dict(
  name = 'Sonu',
  age = 12,
  city = 'begusarai'
)
print(student_2)



print()
# empty dict
d = {}
d = dict()

print(type({}))
print(type(dict()))



# Key point for interviews: Python dictionaries use a hash table, which gives average O(1) performance for lookup, insertion, update, and deletion, while iteration and copying require visiting elements, so they are O(n).