course = ['history', 'Math', 'Physics', 'CompSci']
nums = [2,5,4,7,2,-3,0,44]


# how we can find some value here within our list so, if we wanted to find the index of a certain value then we can use the index method or .index() 
print(course.index('Math')) 
# print(course.index('math')) #gives ValueError

print()

# if we simply check is our value in our list or not then, we use the in operator it give T/F
print('art' in course)
print('Chemistory' in course)
print('Physics' in course)

print()

#for loop -- here we are looping through each value of our list and printing each time 
for total_subject in course:
  print(total_subject)

print() 

# printing with index 
for index, subject_cource in enumerate(course):
  print(index, subject_cource)

print()

for index, subject_cource in enumerate(course, start=1): #if we want to start at 1 then use start
  print(index, subject_cource)


print()


#spilliting value
# convert list into string seperated by a certain value -- we use string method called join
course_str = ', '.join(course)
course_str = ' - '.join(course)
print(course_str)

#how back to the original list using split() method
new_list = course_str.split(' - ')
print(new_list)
