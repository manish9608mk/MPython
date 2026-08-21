# organizing a list using -- sort() method for permanently 0r sorted() function for temporarily 

course = ['history', 'Math', 'Physics', 'CompSci']
nums = [2,5,4,7,2,-3,0,44]

# permanently
print(course)
course.sort()
print(course) # in alphabetical order sorted
course.sort(reverse=True) #in decending order simple way or we can use reverse method ie. below
print(course)
nums.sort()  # in accending order
print(nums)

print()

#temporarily 
print(course)
print(sorted(course)) #or we can stored in new variable ie. sorted_course then pass in print()
print(course)
print(sorted(nums))

print()

#reverse() method
course.reverse()  #printing a list in reverse order
print(course)
nums.reverse()
print(nums)