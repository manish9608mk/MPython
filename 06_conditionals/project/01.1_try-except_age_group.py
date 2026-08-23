
'''
syntax ---->

try:
    # Risky code

except ErrorType:
    # Error handle karne wala code

'''

# Method 2 (recommended)
try:
  age = int(input('Please enter your age: '))

  if age < 13:
    print('child')
  elif age < 20:
    print('teenager')  
  elif age < 60:
    print('adult')
  else:
    print('senior')
      
  print('Hey, Your age is: ' + str(age)) # + Operator
  print("Your age is:", age) # Comma ,
  print(f'Bro your age is: {age}') # f-string (Most Recommended)

except ValueError:
  print('invalid Input')




print("---------------------------------------")
# Method 3 --- indentation ka dhayan do always in py
try:
  age = int(input('Please enter your age: '))

except ValueError:
  print('invalid Input')
  exit()


if age < 13:
  print('child')
elif age < 20:
  print('teenager')  
elif age < 60:
  print('adult')
else:
  print('senior')
    
print('Hey, Your age is: ' + str(age)) # + Operator
print("Your age is:", age) # Comma ,
print(f'Bro your age is: {age}') # f-string (Most Recommended)



# use try except to: 
# Handle invalid user input and prevent the program from crashing.
# Use try-except to catch ValueError if the user enters an invalid integer.
# If the user enters something other than an integer, handle the error gracefully.
# Handle invalid input (e.g., letters or special characters) entered by the user.
# Use try-except to handle invalid user input and prevent the program from crashing.
