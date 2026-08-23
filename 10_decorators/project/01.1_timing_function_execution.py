'''
Problem 1: Timing Function Execution

Create a decorator that measures how much time a function
takes to execute.

Decorator
    ↓
Adds extra functionality to an existing function
without changing the function's original code.

Goal:
    Measure the execution time of any function.

Basic flow:

    function()
        ↓
    decorator
        ↓
    record start time
        ↓
    execute function
        ↓
    record end time
        ↓
    calculate execution time
        ↓
    display/return the result

Important:
- Use a decorator to wrap the original function.
- Use time.perf_counter() to measure execution time.
- The decorator should work with functions that may have
  different arguments.
- Use *args and **kwargs so the wrapper can accept any
  positional and keyword arguments.
- The original function should still return its result.

In simple words:

    Before function → Start timer
    Function runs
    After function  → Stop timer
    Difference      → Execution time

Real-world use:
- Measuring API response time
- Checking database query performance
- Finding slow functions
- Performance testing and optimization

Example:

    @timer
    def calculate():
        ...

When calculate() is called:

    timer
      ↓
    start time
      ↓
    calculate()
      ↓
    end time
      ↓
    print execution time
'''


import time

def timer(func):

  def wrapper(*args, **kwargs):

    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()

    print(f'{func.__name__} ran in {end-start} time')

    return result
  
  return wrapper

@timer
def example_function(n):
  time.sleep(n)
example_function(3)
