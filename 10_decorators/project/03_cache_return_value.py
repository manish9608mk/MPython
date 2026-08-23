'''
Problem 3: Cache Return Values

Create a decorator that caches the return value of a function.

Goal:
    If a function is called again with the same arguments,
    return the previously calculated result instead of
    executing the function again.

Basic idea:

    First call
        ↓
    Function executes
        ↓
    Result is stored in cache
        ↓
    Result returned

    Same arguments again
        ↓
    Check cache
        ↓
    Result found
        ↓
    Return cached result
        ↓
    Function does NOT execute again

Example:

    @cache
    def square(n):
        return n * n

    square(5)    → function executes → result is cached
    square(5)    → cached result returned
    square(10)   → function executes → result is cached

Important:
- Use a dictionary to store cached results.
- Function arguments can be used as dictionary keys.
- Check whether the arguments already exist in the cache.
- If found → return the cached value.
- If not found → execute the function.
- Store the new result in the cache.
- Return the result.

Basic flow:

    function call
        ↓
    wrapper(*args, **kwargs)
        ↓
    Is result already cached?
       / \
     Yes  No
      ↓    ↓
    return  execute function
    cache       ↓
              store result
                 ↓
              return result

Real-world use:
- Expensive calculations
- Database/API results
- Recursive algorithms
- Avoiding repeated computation
- Improving application performance

In simple words:

    Same input
        ↓
    Same result
        ↓
    Don't calculate again
        ↓
    Return stored result

This technique is called:
    Memoization / Caching
'''


# import time

# def cache(func):
#   cache_value = {}
#   print(cache_value)
#   def wrapper(*args):
#     if args in cache_value:
#       return cache_value[args]
#     result = func(*args)
#     cache_value[args] = result
#     return result
#   return wrapper

# @cache
# def long_long_running(a, b):
#   time.sleep(4)
#   return a + b

# print(long_long_running(2,3))
# print(long_long_running(2,3))
# print(long_long_running(4,5))



import time


def cache(func):

  # Dictionary used to store previously calculated results.
  #
  # Example:
  # {
  #   (2, 3): 5,
  #   (4, 5): 9
  # }
  cache_value = {}

  # Wrapper receives the arguments passed to the original function.
  def wrapper(*args, **kwargs):

    # Check whether these arguments were already used.
    if args in cache_value:
      print('Returning cached result')

      # Return the previously calculated result.
      return cache_value[args]

    # Arguments are not present in cache,
    # so execute the original function.
    print('Executing function')

    result = func(*args, **kwargs)

    # Store the result so that the same arguments
    # can use the cached value next time.
    cache_value[args] = result

    return result

  return wrapper


@cache
def long_long_running(a, b):

  # Simulate an expensive/slow operation.
  time.sleep(4)

  return a + b


print(long_long_running(2, 3))
print(long_long_running(2, 3))
print(long_long_running(4, 5))