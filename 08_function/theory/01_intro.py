'''
A function is a reusable block of code that performs a specific task.

Input
   │
   ▼
+------------------+
|    Function      |
|   Does a Task    |
+------------------+
   │
   ▼
Output

syntax: create a function using def keyword
def function_name():
    # code

function_name()   # calling function 



| Concept       | Meaning                             |
| ------------- | ----------------------------------- |
| Function      | A reusable block of code            |
| `def`         | Creates a function                  |
| Function Call | Executes the function               |
| Parameter     | Input to the function               |
| Argument      | Actual value passed to the function |
| `return`      | Sends a value back                  |

'''


# eg1 - hard coding
def greet():
    print("Hello rahul")

greet()




print()
# eg2 : Functions With Parameters - Instead of hardcoding: Use a parameter.
# A parameter is a variable that receives data.
# here we can also use Multiple Parameters 

def hello(name):  # name is the parameter.
    print('hello', name)

hello('rahul') # 'rahul' is called the argument.
hello('manish')
hello('sonu')
greet()
# Inside function - parameter, outside function - argument




print()
# eg3 : Functions With Return Value - return sends the result back to the caller.

def add (a , b):
    return (a + b)

print(add) # Prints the function object or memory address

add_result = add(5 , 5)
print(add_result) # 10
# or,
print(add(10 , 10)) # 20
    


