# Reverse a string using a loop.

# Method 1: Build a new string
# TC - O(n²), Because strings are immutable in Python. Every char + reversed_str creates a new string.

input_str = input('\nEnter a string you want to reverse : ').strip().lower()
reversed_str = ''

for char in input_str: 
  reversed_str = char + reversed_str

print(f"Reversed stringM1 : {reversed_str}")










print()
# Method 2: Using Index (range)
# TC - O(n)

input_str = input("Enter a stringM2 : ")

for i in range(len(input_str) - 1, -1, -1):
    print(input_str[i], end="")










print()
# Method 3: Store in another string using index , TC - O(n²)

input_str = input("\nEnter a stringM3 : ")

reversed_str = ""

for i in range(len(input_str) - 1, -1, -1):
    reversed_str += input_str[i]

print(reversed_str)









print()
# Method 4: Using a List (Most Efficient Loop Approach), TC - O(n)
input_str = input("Enter a stringM4 : ")

chars = []

for i in range(len(input_str) - 1, -1, -1):
    chars.append(input_str[i])

reversed_str = "".join(chars)

print(reversed_str)









print()
# Method 5: Using reversed()
input_str = input("Enter a stringM5 : ")

print("".join(reversed(input_str)))










print()
# Method 6: Using Slicing (Most Pythonic)
input_str = input("Enter a stringM6 : ")

print(input_str[::-1])









print()
# Method 7: Using a While Loop
input_str = input("Enter a stringM7 : ")

i = len(input_str) - 1

while i >= 0:
    print(input_str[i], end="")
    i -= 1










print()
# Method 8: Using Recursion (Advanced)
def reverse(s):
    if s == "":
        return ""
    return reverse(s[1:]) + s[0]

print(reverse(input("\nEnter a stringM8 : ")))
