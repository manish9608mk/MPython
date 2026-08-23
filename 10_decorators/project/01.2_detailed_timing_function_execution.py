'''
Problem 1: Timing Function Execution

Create a decorator that measures how much time a function
takes to execute.

Key idea:
    Decorator → adds extra behavior to an existing function
    without modifying the original function's code.

Here, the extra behavior is:
    Measuring the function's execution time.

Flow:

    @timer
       ↓
    timer(func)
       ↓
    wrapper(*args, **kwargs)
       ↓
    record start time
       ↓
    execute original function
       ↓
    record end time
       ↓
    calculate execution time
       ↓
    return original function's result

Important:
- time.time() gives the current time.
- *args accepts any positional arguments.
- **kwargs accepts any keyword arguments.
- func(*args, **kwargs) calls the original function.
- The wrapper returns the original function's result.
- func.__name__ gives the original function's name.

Real-world use:
- Measuring API response time
- Measuring database query execution
- Finding slow functions
- Performance testing

In simple words:

    Start timer
        ↓
    Run function
        ↓
    Stop timer
        ↓
    End time - Start time
        ↓
    Execution time
'''


import time


# Decorator function
# Takes the original function as an argument.
def timer(func):

  # Wrapper function
  # *args and **kwargs allow the decorator to work
  # with functions having any number of arguments.
  def wrapper(*args, **kwargs):

    # Record the start time before executing the function.
    start = time.time()

    # Execute the original function and store its result.
    result = func(*args, **kwargs)

    # Record the end time after the function finishes.
    end = time.time()

    # Calculate and display the execution time.
    print(f'{func.__name__} ran in {end - start} seconds')

    # Return the original function's result.
    return result

  # Return the wrapper function.
  return wrapper


# @timer is equivalent to:
# example_function = timer(example_function)
@timer
def example_function(n):
  time.sleep(n)


example_function(3)




'''
The main things you should remember from this problem:

Decorator
   ↓
timer(func)

Wrapper
   ↓
wrapper(*args, **kwargs)

Before function
   ↓
start = time.time()

Run function
   ↓
result = func(*args, **kwargs)

After function
   ↓
end = time.time()

Execution time
   ↓
end - start

Finally
   ↓
return result


One small improvement for production/interview code: prefer time.perf_counter() over time.time() when measuring elapsed execution time.
'''