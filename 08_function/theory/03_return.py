# eg1
def add_one(x):
  return x+1

y = add_one(5) # 6
print(y) 



print()
# eg2 - NONE
def add_one(x):
  print(x+1)

y = add_one(5) # 6
print(y) 



print()
# eg3 - correct eg2 we have to use return type 
def add_one(x):
  print(x+1)
  return x+1

y = add_one(5) # 6
print(y) 




# KKB

# print() - 
# ✔ Displays something on the screen.
# ✔ Does NOT send a value back.
# ✔ Automatically returns None.

# return - 
# ✔ Sends a value back to the caller.
# ✔ Does NOT automatically display anything.
# ✔ Ends the function immediately.