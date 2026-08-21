# how to create empty in -- lists, tuples, sets


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
print(type(empty_set))

empty_set = set() # correct
print(type(empty_set))

# empty dict
d = {}
d = dict()

print(type({}))
print(type(dict()))



print()
#creating sets: 2 methods
colors_1 = {"red","green","blue"}
colors_2 = set(["red","green","blue",'black'])
print(colors_1)
print(colors_2)


print()
print(type([]))       # <class 'list'>
print(type(()))       # <class 'tuple'>
print(type({}))       # <class 'dict'>
print(type(set()))    # <class 'set'>


print()
#Creating a tuple with one element -- This is not a tuple.
t = (5)
print(type(t)) # int

#The correct way is:
t = (5,)
print(type(t)) # tuple
