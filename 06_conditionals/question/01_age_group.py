# age group categorization

# Method 1

# input() hamesha string (str) return karta hai. isliye age ko int banao

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


# NOTE:
# If the user enters an invalid number (such as "dd", "abc", or "12.5"),
# int() cannot convert it to an integer.
# Python will raise a ValueError.
#
# Example:
# Input: dd
# Output:
# ValueError: invalid literal for int() with base 10: 'dd'
# for best method: see 01A_try-except_age_group.py



'''
Input lene ke different method:
| Method       | Example                                          |
| ------------ | ------------------------------------------------ |
| Simple       | `age = int(input())`                             |
| Prompt       | `age = int(input("Enter age: "))`                |
| New Line     | `age = int(input("Enter age:\n"))`               |
| Variable     | `msg = "Enter age: "`<br>`age = int(input(msg))` |
| f-string     | `age = int(input(f"{name}, enter age: "))`       |
| String First | `age = input("Enter age: ")`                     |
| `.strip()`   | `age = int(input("Enter age: ").strip())`        |
| Exception    | `try: age = int(input(...))`                     |

'''