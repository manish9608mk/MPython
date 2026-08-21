# RECURSION

# Recursion:
# A programming technique in which a function calls itself.

# Recursive Function:
# A function that calls itself.

# Every recursive function has two parts:
# 1. Base Case (Stopping Condition) - without Base Case recursion become infinite(stack full - LIFO) so, Every recursive function must have a stopping condition
# 2. Recursive Call (Function calls itself)

# Without a Base Case, you'll get a RecursionError.
# Always find the Base Case first.
# Every recursive call should make the problem smaller (n-1, index+1, etc.).
# Every recursive call should move closer to the Base Case.
# Recursion is not just a function calling itself.
# It keeps reducing the problem into smaller parts until the Base Case is reached.



# Example 1 : Print "Hi" 5 Times
def hello(n):

    # base case : Stops recursion.
    if n == 0:
        return

    print('Hi')

    # Recursive Call : Function calls itself.
    hello(n - 1)

hello(5)
print()


# Example 2 : Countdown
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)

countdown(5)


# Example 3 : Count Up
print()

def count_up(n):

    if n == 0:
        return
    
    count_up(n-1)
    print(n)

count_up(5)    
# here, The recursive call happens before print(), so the numbers are printed while returning from recursion.





'''
Golden Formula

def function(problem):

    # 1. Base Case
    if problem is solved:
        return

    # 2. Work

    # 3. Smaller Problem
    function(smaller_problem)
'''