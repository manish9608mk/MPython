# Prime Number Checker
# Check whether a given number is prime or not.
# A prime number has exactly two factors: 1 and itself.
'''2
Logic:
1. Prime numbers are greater than 1.
2. Check divisibility from 2 to n-1 (or √n for the optimal solution).
3. If any number divides n exactly, it is NOT prime.
4. Otherwise, it is PRIME.

Brute Force : Check from 2 to n-1      → O(n)
Optimal     : Check from 2 to √n       → O(√n) 
'''

# method1
number = int(input('Enter natural number : '))

is_prime = True

if number > 1:

  for i in range (2 , number):
    if (number % i) == 0:
      is_prime = False
      break

print(f'{is_prime}')  



# method2 : Flag Pattern 

number = int(input("\nEnter a natural number: "))

is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a Prime Number.")
else:
    print(f"{number} is Not a Prime Number.")











