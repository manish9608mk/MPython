'''
===========================================================
                    PYTHON DECORATORS
===========================================================

A decorator is a function that adds extra behavior to
another function WITHOUT changing the original function's
code.

Think of it like:

    Original Function
          ↓
      Decorator
          ↓
    Extra Behavior
          ↓
    Modified Function

Common uses:
    - Logging
    - Debugging
    - Timing
    - Authentication / Authorization
    - Caching / Memoization
    - Validation
    - Monitoring

===========================================================
1. FUNCTIONS ARE FIRST-CLASS OBJECTS
===========================================================

In Python, functions are objects.

Therefore, we can:

    1. Store a function in a variable
    2. Pass a function as an argument
    3. Return a function from another function
'''


# ---------------------------------------------------------
# 1. Function stored in a variable
# ---------------------------------------------------------

def greet():
    print("Hello!")


my_function = greet

my_function()
# Output:
# Hello!


# ---------------------------------------------------------
# 2. Function passed as an argument
# ---------------------------------------------------------

def say_hello():
    print("Hello")


def execute_function(func):
    func()


execute_function(say_hello)
# Output:
# Hello


'''
IMPORTANT:

This concept is the FOUNDATION of decorators.

A decorator receives a function as an argument.

        decorator(function)
                ↓
        returns new function
'''


# =========================================================
# 2. FUNCTION RETURNING ANOTHER FUNCTION
# =========================================================

def outer():

    def inner():
        print("Inside inner function")

    return inner


result = outer()

result()
# Output:
# Inside inner function


'''
Here:

    outer()
       ↓
    returns inner

So:

    result = outer()

means:

    result = inner

Then:

    result()

calls inner().


This concept is also very important for decorators.
'''


# =========================================================
# 3. SIMPLE DECORATOR
# =========================================================

'''
A decorator usually has this structure:

    def decorator(func):

        def wrapper():
            # Extra behavior

            func()

            # More extra behavior

        return wrapper


The wrapper function "wraps" the original function.
'''


def decorator(func):

    def wrapper():

        print("Before function")

        func()

        print("After function")

    return wrapper


def hello():
    print("Hello!")


# Manually decorating the function

hello = decorator(hello)

hello()

'''
Output:

Before function
Hello!
After function
'''


# =========================================================
# 4. USING @ SYNTAX
# =========================================================

'''
Instead of:

    hello = decorator(hello)

Python provides:

    @decorator

So:

    @decorator
    def hello():
        print("Hello")

is equivalent to:

    def hello():
        print("Hello")

    hello = decorator(hello)
'''


def my_decorator(func):

    def wrapper():

        print("Before")

        func()

        print("After")

    return wrapper


@my_decorator
def hello():
    print("Hello")


hello()


# =========================================================
# 5. DECORATOR FLOW
# =========================================================

'''
When Python sees:

    @my_decorator
    def hello():
        print("Hello")

Python internally does:

    def hello():
        print("Hello")

    hello = my_decorator(hello)


So:

    hello
      ↓
    my_decorator(hello)
      ↓
    wrapper
      ↓
    hello() actually calls wrapper()
'''


# =========================================================
# 6. WHY DO WE NEED wrapper()?
# =========================================================

'''
The wrapper allows us to add extra behavior.

Example:

    @timer
    def calculate():
        ...

The decorator can do:

    Start timer
         ↓
    calculate()
         ↓
    Stop timer


The original calculate() function does not need
to contain timer-related code.
'''


# =========================================================
# 7. DECORATOR WITH FUNCTION ARGUMENTS
# =========================================================

'''
Problem:

Our previous wrapper was:

    def wrapper():
        func()

But what if the original function requires arguments?

Example:

    def add(a, b):
        return a + b

The wrapper must be able to receive those arguments.
'''


def decorator_with_args(func):

    def wrapper(*args, **kwargs):

        print("Arguments:", args)
        print("Keyword arguments:", kwargs)

        result = func(*args, **kwargs)

        return result

    return wrapper


@decorator_with_args
def add(a, b):
    return a + b


print(add(10, 20))


'''
IMPORTANT:

    *args
        ↓
    captures positional arguments

    **kwargs
        ↓
    captures keyword arguments


Example:

    add(10, 20)

becomes:

    args = (10, 20)
    kwargs = {}


Example:

    greet(name="Manish")

becomes:

    args = ()
    kwargs = {"name": "Manish"}
'''


# =========================================================
# 8. WHY *args AND **kwargs?
# =========================================================

'''
Because a decorator should ideally work with different
types of functions.

For example:

    function1()
    function2(10)
    function3(10, 20)
    function4(name="Manish")
    function5(10, name="Manish")

Using:

    wrapper(*args, **kwargs)

allows the decorator to handle all of them.
'''


# =========================================================
# 9. RETURN THE ORIGINAL FUNCTION'S RESULT
# =========================================================

'''
Very important:

The wrapper should normally return the result of
the original function.

Correct:

    result = func(*args, **kwargs)
    return result

or simply:

    return func(*args, **kwargs)


Otherwise, the decorated function may return None.
'''


def decorator_return(func):

    def wrapper(*args, **kwargs):

        print("Function is running")

        return func(*args, **kwargs)

    return wrapper


@decorator_return
def multiply(a, b):
    return a * b


result = multiply(5, 4)

print(result)
# Output:
# Function is running
# 20


# =========================================================
# 10. REAL EXAMPLE — TIMING
# =========================================================

'''
A decorator can measure how long a function takes.
'''

import time


def timer(func):

    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(
            f"{func.__name__} took "
            f"{end - start:.6f} seconds"
        )

        return result

    return wrapper


@timer
def slow_function():
    time.sleep(1)
    return "Done"


print(slow_function())


'''
Flow:

slow_function()
       ↓
wrapper()
       ↓
start timer
       ↓
original slow_function()
       ↓
stop timer
       ↓
print execution time
       ↓
return result
'''


# =========================================================
# 11. REAL EXAMPLE — DEBUGGING
# =========================================================

def debug(func):

    def wrapper(*args, **kwargs):

        print(f"Calling function: {func.__name__}")
        print(f"Positional arguments: {args}")
        print(f"Keyword arguments: {kwargs}")

        result = func(*args, **kwargs)

        return result

    return wrapper


@debug
def greet(name, greeting="Hello"):

    return f"{greeting}, {name}"


print(greet("Manish", greeting="Hi"))


# =========================================================
# 12. REAL EXAMPLE — CACHING / MEMOIZATION
# =========================================================

'''
Caching means:

If the same input is given again,
don't calculate the result again.

Instead:

    return the previously stored result.
'''


def cache(func):

    cache_data = {}

    def wrapper(*args):

        if args in cache_data:

            print("Returning cached result")

            return cache_data[args]

        print("Calculating result")

        result = func(*args)

        cache_data[args] = result

        return result

    return wrapper


@cache
def square(n):

    time.sleep(1)

    return n * n


print(square(5))
print(square(5))
print(square(10))


'''
First:

    square(5)

        ↓

    Not in cache

        ↓

    Calculate 25

        ↓

    Store:

        (5) → 25


Second:

    square(5)

        ↓

    Found in cache

        ↓

    Return 25

        ↓

    Function does NOT execute again.


This is called:

    Caching
    Memoization
'''


# =========================================================
# 13. functools.wraps
# =========================================================

'''
Problem:

When a function is decorated, the function's metadata
can be replaced by the wrapper's metadata.

Python provides:

    functools.wraps

to preserve the original function's metadata.
'''

from functools import wraps


def better_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        return func(*args, **kwargs)

    return wrapper


@better_decorator
def addition(a, b):
    """Return the sum of two numbers."""

    return a + b


print(addition(10, 20))

print(addition.__name__)
# addition

print(addition.__doc__)
# Return the sum of two numbers.


'''
BEST PRACTICE:

When writing reusable decorators:

    from functools import wraps

    @wraps(func)

Use this in the wrapper.
'''


# =========================================================
# 14. DECORATOR WITH PARAMETERS
# =========================================================

'''
Sometimes we want:

    @repeat(3)

instead of:

    @repeat
'''


def repeat(times):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for _ in range(times):

                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


@repeat(3)
def say_hello():

    print("Hello")


say_hello()


'''
Notice the three levels:

    repeat(times)
        ↓
    decorator(func)
        ↓
    wrapper(*args, **kwargs)


Why?

Because @repeat(3) must first receive 3.

Then it receives the function.

Then wrapper receives the function's arguments.
'''


# =========================================================
# 15. THE DECORATOR TEMPLATE
# =========================================================

'''
Memorize this basic template:

    from functools import wraps

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            # BEFORE

            result = func(*args, **kwargs)

            # AFTER

            return result

        return wrapper


    @decorator
    def function(...):
        ...


Think:

    decorator
        ↓
    receives function

    wrapper
        ↓
    receives function arguments

    func(*args, **kwargs)
        ↓
    runs original function
'''


# =========================================================
# 16. THE MOST IMPORTANT CONCEPT
# =========================================================

'''
If you remember only one thing, remember this:

    @decorator
    def function():
        ...


means:

    function = decorator(function)


And if decorator is:

    def decorator(func):

        def wrapper(*args, **kwargs):

            # extra behavior

            return func(*args, **kwargs)

        return wrapper


then:

    function()

actually calls:

    wrapper()

and wrapper() eventually calls:

    func()


Complete mental model:

        @decorator
             ↓
    decorator(original_function)
             ↓
          wrapper
             ↓
      function() called
             ↓
          wrapper()
             ↓
      extra behavior
             ↓
    original function()
             ↓
          result
'''


# =========================================================
# 17. QUICK REVISION
# =========================================================

'''
DECORATOR CHEAT SHEET
---------------------

Decorator:
    A function that modifies/adds behavior to another function.

Basic syntax:

    def decorator(func):

        def wrapper(*args, **kwargs):

            return func(*args, **kwargs)

        return wrapper


Using decorator:

    @decorator
    def function():
        ...


Equivalent:

    function = decorator(function)


Important concepts:

    func
        → original function

    wrapper
        → new function that surrounds original function

    *args
        → positional arguments

    **kwargs
        → keyword arguments

    func(*args, **kwargs)
        → calls original function

    return result
        → preserves original return value

    @wraps(func)
        → preserves function metadata


Common uses:

    @timer
        → measure execution time

    @debug
        → inspect function calls

    @cache
        → avoid repeated calculations

    @login_required
        → authentication

    @validate
        → input validation


MOST IMPORTANT LINE:

    @decorator

means:

    function = decorator(function)
'''


# =========================================================
# FINAL MENTAL MODEL
# =========================================================

'''
Imagine a function is a person entering a building.

Original function:

        [ FUNCTION ]

Decorator is a security gate around it:

        ┌──────────────────────┐
        │      DECORATOR       │
        │                      │
        │   [ FUNCTION ]       │
        │                      │
        └──────────────────────┘

The function itself doesn't change.

The decorator adds something around it:

        Before
           ↓
      Function runs
           ↓
        After


Therefore:

    DECORATOR = "Add behavior around an existing function
                 without changing its original code."
'''