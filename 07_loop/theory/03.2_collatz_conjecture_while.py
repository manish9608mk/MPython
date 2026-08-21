# beware of infinity!

# Keep in mind that it has not been mathematically proven that this loop will always terminate.
# Warning: It has not been mathematically proven that this sequence always reaches 1,
# so there is no guarantee that this loop will terminate for every positive integer.

# meaning of Conjecture: A conjecture is a statement that appears to be true based on many examples, but it has not been mathematically proven.

'''
This is a famous mathematical sequence called the Collatz Conjecture (also known as the 3n + 1 Problem).

-- Time Complexity --
There is no known formula for exactly how many steps it takes for any starting number to reach 1.

So, unlike many algorithms, there isn't a simple Big-O expression based on n.

For practical inputs, it eventually reaches 1 for all numbers that have been tested, but no one has proved that this is always true for every positive integer. That's why it's called the Collatz Conjecture — it's an unsolved problem in mathematics.

-- Loop Pattern Used --
This program is an example of a Simulation Pattern.

Why?

- We start with an initial value (n = 27).
- We repeatedly apply a rule.
- The state (n) changes every iteration.
- The loop stops when a condition (n == 1) is reached.

This is the same loop pattern used in simulations like retry logic, traffic lights, games, and ATM state machines.
'''

n = 27

while n != 1:
  print(n)

  if n % 2 == 0: # n is even 
    n = n // 2
  else:
    n = n * 3 + 1 # n is odd

print(n)    






# infinite loop example 
# Stop using - Control (⌃) + C
# while True means:
# "Keep running forever."

# while True:
#     print("This loop never ends.")


