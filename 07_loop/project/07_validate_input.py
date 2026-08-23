# Validate input
# Keep asking the user for input until they enter a number between 1 and 10.

'''
Examples:

Input : 0
Output: Invalid! Try again.

Input : 15
Output: Invalid! Try again.

Input : 7
Output: Valid input: 7
'''

# method1
while True:
  number = int(input('Enter a number between 1 to 10 : '))

  if 1 <= number <= 10:
    print('\nThanks')
    break
  else:
    print('Invalid number!!, please enter correct number')

'''
Method 1: Range Validation Only
-----------
Use an infinite loop (while True).

1. Ask the user for input.
2. Convert it to an integer.
3. Check if the number is between 1 and 10.
4. If valid:
      - Print success message.
      - break the loop.
5. Otherwise:
      - Print an error message.
      - Loop continues and asks again.

Note:
This method assumes the user enters only numbers.
If the user enters letters (e.g. "abc"),
the program will crash with ValueError.
'''

# method2 
while True:
    try:
        number = int(input("Enter a number between 1 to 10 : "))

        if 1 <= number <= 10:
            print("\nThanks for validating")
            break
        else:
            print("Invalid number!! Please enter a number between 1 and 10.")

    except ValueError:
        print("Enter numbers only, not characters.")


'''
Method 2: Range Validation + Exception Handling (Recommended)
-----------
Use while True with try-except.

1. Keep asking for input.
2. Try converting the input to an integer.
3. If conversion succeeds:
      - Check if the number is between 1 and 10.
      - If valid:
            Print success message.
            break the loop.
      - Else:
            Print invalid range message.
4. If conversion fails (letters/symbols):
      - except ValueError runs.
      - Print "Enter numbers only."
      - Loop continues.

Why use this method?
--------------------
✔ Handles invalid range.
✔ Handles invalid data type.
✔ Prevents program from crashing.
✔ Best practice for user input.
'''