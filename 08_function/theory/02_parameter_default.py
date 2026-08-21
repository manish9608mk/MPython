# Example 1 : Parameter
def murph(mood):
  # code here gets executed when you call the function
  print (mood)

  if mood == 'happy':
    print('I am happy.')
  else:
    print('I am not happy..')

murph('happy')    
murph('sad')
# print(mood) #NameError: name 'mood' is not defined - outside function scope






print()
# Example 2 : Default Parameter - here we set mood = 'happy'
# Python uses the default value: mood = "happy"
# A default parameter has a default value.
# If no argument is passed, Python uses the default value.

def murph(mood = 'happy'):
  # mood → Parameter
  # "happy" → Default Value
  print (mood)

  if mood == 'happy':
    print('I am happy.')
  else:
    print('I am not happy..')

murph()    
murph('sad')

# Example 2 : Default Parameter
print()
def greet(name="Steve"):
    print("Hello", name)

greet()

greet("Manish")