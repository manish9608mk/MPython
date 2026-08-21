'''
python reads in this order 
LEGB
Local scope, Enclosing scope, Global scope, Built-in scope
'''

# VARIABLE SCOPE IN PYTHON : 
# Scope means:
# The region where a variable can be accessed.

# There are mainly two types:
# 1. Global Variable
# 2. Local Variable

# Rule:
# When Python accesses a variable:
# 1. Search in the Local Scope.
# 2. If not found, search in the Global Scope.
# 3. If still not found, raise NameError.




# Example 1
# Global Variable : 
# A global variable is created outside every
# function and can be read inside functions.

name = "Steve"  # global

def greet():
    print(name)

greet()
print(name)




# Example 2
# Local Variable : 
# A local variable is created inside a function.
# It exists only while that function is running.
print()

def greet():

    name = "manish"  # local

    print(name)

greet()




print()
# Example 3
# Variable Shadowing
# A local variable hides (shadows) the global variable.

x = 100
def test():
    x = 50
    print(x)

test()   # 50
print(x) # 100




print()
# Example 4 : global Keyword
# The global keyword is used inside a function to access and modify a global variable.
# try to avoid global keyword

x = 100
def test():

    global x

    x = x + 1
    print(x)

print(x) # 100
test()   # 101
print(x) # 101

'''
When to Use?

✅ Small scripts
✅ Configuration values (occasionally)
❌ Large projects
❌ Production code
❌ Frequently changing shared state

Instead of global, it's usually better to pass values as parameters and return the updated value.

Interview Question
Q. Why should we avoid using global?
Answer:
Because any function can modify the global variable, making the program harder to understand, debug, and maintain.
'''




"""
=========================
Scope Rules
=========================

Global Variable
- Created outside a function.
- Can be read inside functions.
- Lives until the program ends.

Local Variable
- Created inside a function.
- Exists only while the function runs.
- Cannot be accessed outside the function.

=========================
Important Rules
=========================

✔ Read global variable inside function → Allowed

✔ Create variable inside function → Local Variable

✔ Local variable outside function → NameError

✔ Local and global have same name → Local variable is used (Shadowing)

✔ Modify global variable without 'global' → UnboundLocalError (if you read and assign it in the same function)

✔ Modify global variable with 'global' → Allowed

=========================
Interview Tips
=========================

✔ Prefer local variables.

✔ Avoid global unless necessary.

✔ Local variables make code safer and easier to debug.
"""
