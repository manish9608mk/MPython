# ex2 - with user input 

def multiply(a, b):
    return a * b

try:
    value1 = input("Enter first value: ")
    value2 = input("Enter second value: ")

    # Convert numeric input to integer
    if value1.isdigit():
        value1 = int(value1)

    if value2.isdigit():
        value2 = int(value2)

    # Check for invalid case
    if isinstance(value1, str) and isinstance(value2, str):
        print("Error! You cannot multiply one string by another string in python.")

    else:
        result = multiply(value1, value2)
        print(f"Multiplication of {value1} and {value2} is: {result}")

except Exception as e:   # e stores the actual error.
    print("Something went wrong!")
    print(e)




# 💡 Rule yaad rakhna

# try-except tab use karo jab tum expect karte ho ki koi operation fail ho sakta hai, jaise:

# int(input()) → ValueError
# 10 / num → ZeroDivisionError
# my_list[index] → IndexError
# File open karna → FileNotFoundError

# Is question mein humne pehle hi isdigit() aur isinstance() se invalid cases handle kar diye hain, isliye except ki zarurat nahi bachi.





'''

isdigit() checks whether all characters in a string are digits (0 to 9 only) not -ve and decimal number.

It returns:
True → If the string contains only digits.
False → Otherwise.

Note: isdigit() works only on strings.

-----------------------------------------------------

isinstance() checks whether a variable is an object of a particular data type

It returns:

True
False

syntax:
isinstance(object, datatype)








Easy Memory Trick :

isdigit()

Question:
"Does this STRING contain only digits?"

Example:
"123"  → True
"12a"  → False


-----------------------------------

isinstance()

Question:
"What is the DATA TYPE of this object?"

10          → int
"Hello"     → str
[1,2,3]     → list
{"a": 1}    → dict

''' 