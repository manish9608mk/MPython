# Exponential Backoff
# Double the waiting time after each retry, starting from 1 second.
# Stop retrying after 5 attempts.
# Exponential Backoff is a retry strategy where the waiting time doubles after each failed attempt to reduce system load and improve the chances of success.

'''
Example:

Retry 1 -> Wait 1 second
Retry 2 -> Wait 2 seconds
Retry 3 -> Wait 4 seconds
Retry 4 -> Wait 8 seconds
Retry 5 -> Wait 16 seconds

Explanation:
Start with a wait time of 1 second.
After each retry, double the wait time.
Stop after completing 5 retries.



REAL WORLD EXAMPLE: 
Suppose an AWS application tries to access a database.

Database unavailable ❌

Retry after 1 second
Retry after 2 seconds
Retry after 4 seconds
Retry after 8 seconds
Retry after 16 seconds

If the database comes back online, the request succeeds.

This is widely used in:

AWS
Google Cloud
Azure
Kubernetes
APIs
Microservices
'''


import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
  # print(f'attempt {attempts +1}, waittime {wait_time}')
  print(f"Attempt {attempts + 1}: Waiting {wait_time} second(s)...")
  time.sleep(wait_time)
  wait_time *= 2
  attempts += 1 

print("Maximum retry limit reached.")



#You'll encounter this pattern again in:
# - Binary Exponentiation
# - Binary Search (reducing the search space)
# - Dynamic Programming
# - Retry mechanisms in Cloud/DevOps (AWS, Kubernetes, APIs)
# So although this looks like a simple loop exercise, it introduces a concept that is used in real production systems.