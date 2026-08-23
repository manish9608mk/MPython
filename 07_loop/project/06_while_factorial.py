# Compute the factorial of a given number using a while loop.
# Take a number as input and calculate its factorial using a while loop.
'''
Input: 5
Output: 120

Explanation:
5! = 5 x 4 x 3 x 2 x 1 = 120

'''

# method1 - handle only non-negative integers
number = int(input('Enter any non-negative integers : '))
original_number = number

factorial = 1

while number > 0:
  # factorial = factorial * number
  # number = number - 1
  factorial *= number
  number -= 1

print(f'factorial of {original_number} is : {factorial}')







# method2 - handle for any  integer 
number = int(input("\nEnter any integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    original_number = number
    factorial = 1

    while number > 0:
        factorial *= number
        number -= 1

    print(f"Factorial of {original_number} is: {factorial}")