# sum of even numbers 
# calculate the sum of even numbers up to given number n

# user number or given number by user called n 
n = int(input('Enter a number : '))
# in beginning sum is zero so, 
sum_of_even_number = 0

# i is the loop variable. You can use any valid variable name.
for i in range(1, n+1): 
  if i % 2 == 0:
    sum_of_even_number += i

print(f'Sum of even number upto {n} is : {sum_of_even_number}')    












print()

# in this question we can also use try except 
# Handle invalid user input and prevent the program from crashing.
# Use try-except to catch ValueError if the user enters an invalid integer.
# If the user enters something other than an integer, handle the error gracefully.
# Handle invalid input (e.g., letters or special characters) entered by the user.
# Use try-except to handle invalid user input and prevent the program from crashing.


try:
    n = int(input("Enter a positive number: "))

    if n <= 0:
        print("Please enter a positive number.")
    else:
        even_sum = 0

        for i in range(2, n + 1, 2):
            even_sum += i

        print(f"Sum of even numbers up to {n} is: {even_sum}")

except ValueError:
    print("Please enter a valid integer.")