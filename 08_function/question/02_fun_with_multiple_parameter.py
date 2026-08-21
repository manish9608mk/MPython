# function with multiple parameters
# Create a function that takes two numbers as parameters and returns their sum.

# Ex1 - without user input
def add(a,b):
  return a + b

result = add(5,6)
print(result)     # Prints the returned value.
print(add)        # Prints the function object (its information and memory address).



print()
# Ex2 - With user input using try-except (input handling)
def add(a,b):
  return a + b

try:
    
  num1 = int(input('Enter first number: '))
  num2 = int(input('Enter second number: '))

  result = add(num1,num2)
  print(f'Sum of {num1} and {num2} is : {result}') 
  # or, directly
  # print(f"Sum of {num1} and {num2} is : {add(num1, num2)}")

except ValueError:
  print('Invalid input! please enter valid integers.')






'''
IN ABOVE EXAMPLE: Ex1

Memory
0x1007f9080
──────────────
Function Object
Name : add
Code : return a + b
──────────────

print(add)

'add' is the function object, not a function call.
Since there are no parentheses (), Python does not execute the function.

Instead, Python prints information about the function object,
including its memory address.

Example Output:
<function add at 0x1007f9080>

The memory address (0x1007f9080) is where the function object is
stored in the computer's memory (RAM).

This address may be different every time you run the program because
the operating system can allocate a different memory location each time.

To execute the function, use parentheses:
print(add(5, 6))   # Output: 11

Easy Memory Trick: 
add
↓
Function Object

add()
↓
Function Call

print(add)
↓
Prints information about the function

print(add())
↓
Executes the function
'''     