
# and
print('\n============ and =============')


user = 'admin'
logged_in = True
# logged_in = False 

if user == 'admin' and logged_in:
  print('Admin page')
else:
  print('Bad credientials')






# or 
print('============ or ==============')


user = 'admin'
logged_in = False

if user == 'admin' or logged_in:
  print('Admin page')
else:
  print('Bad credientials')







# not -- it just switches that false to a true
print('=================== not ============')


user = 'admin'
logged_in = False

if not logged_in:
  print('Please logged in')
else:
  print('Welcome')








# is keyword -- it is a object identity or address
# two object is actually be equal but not be the same object in memory
print('====================== is =============')


a = [1,2,3]
b = [1,2,3]

print (a == b)
print (a is b)
print(id(a))
print(id(b))


print()

a = [1,2,3]
b = a

print (a == b) 
print (a is b) # now these are the same object in memory
# now id of both a and b is same and conditions are also true 
print(id(a))
print(id(b))





'''

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

'''