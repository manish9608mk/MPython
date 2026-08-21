'''
Problem 2: Debugging Function Calls

Create a decorator that prints the function name and the
values of its arguments every time the function is called.

Goal:
    Whenever a function runs, display:
        1. Function name
        2. Positional arguments (*args)
        3. Keyword arguments (**kwargs)

Example:

    @debug
    def add(a, b):
        return a + b

    add(10, 20)

Output:
    Function: add
    Arguments: (10, 20)

Important:
- Use a decorator to add debugging functionality.
- Use *args to capture positional arguments.
- Use **kwargs to capture keyword arguments.
- Use func.__name__ to get the original function's name.
- Call the original function using:
      func(*args, **kwargs)
- Return the original function's result.

Basic flow:

    function call
        ↓
    @debug
        ↓
    wrapper(*args, **kwargs)
        ↓
    print function name
        ↓
    print arguments
        ↓
    call original function
        ↓
    return result

Real-world use:
- Debugging function calls
- Logging
- Tracking API calls
- Checking what arguments are being passed
- Troubleshooting application behavior

In simple words:

    @debug
        ↓
    "Whenever this function is called,
     show me its name and arguments."
'''


def debug(func):
  
  def wrapper(*args, **kwargs):

    args_value = ', '.join(str(arg) for arg in args)
    kwargs_value = ', '.join(f'{key} : {value}' for key, value in kwargs.items())

    print(f'calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}')

    return func(*args, **kwargs)
    
  return wrapper


# @debug means:
# hello = debug(hello)
@debug
def hello():
  print('hello')

@debug
def greet(name:str, greeting='Hello') -> None:
  print(f'{greeting}, {name}')

hello()
greet("Manish", greeting="Kaise Ho")





'''
func.__name__       -  function name
*args               - positional arguments
**kwargs            - keyword arguments
'''