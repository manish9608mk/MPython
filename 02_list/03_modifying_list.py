course = ['history', 'Math', 'Physics', 'CompSci']

print(course)
print(len(course))
print()

# Modifying list 
#using append() method -- it added item end of the list 
course.append("Chemistry")
print(course)

print()
#using insert() method -- add new element at any index or position in the list 
course.insert(0 , 'Biology')
print(course)

print()
# using 'del' statement -- removing item from list at any index if we know that position
del course[0]
print(course)

print()
#using pop() method -- removes the last item in a list 
print(course)
popped_course = course.pop()
print (course)
print(popped_course)

print()
#popping item from any position in list 
print(course)
popped_course = course.pop(1)
print(course)

print()
# using remove() method -- removing item by value bcz, sometimes we won't know position 
print(course)
course.remove('CompSci')
print(course)