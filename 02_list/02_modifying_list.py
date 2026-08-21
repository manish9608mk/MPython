course = ['history', 'Math', 'Physics', 'CompSci']
course_2 = ['Organic', 'Physical']

'''
course.insert(0, course_2)
print(course)
print(course[0]) 
'''
print()
#using extend() method 
course.extend(course_2)
print(course)

course.append(course_2)
print(course)
