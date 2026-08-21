def my_decorator(func):

    def wrapper(*args, **kwargs):

        # BEFORE
        # Extra work before the original function

        result = func(*args, **kwargs)

        # AFTER
        # Extra work after the original function

        return result

    return wrapper


@my_decorator
def my_function():
    print("Hello")


my_function()






print()
# ============================================================
# DECORATOR BASIC TEMPLATE
# ============================================================

def my_decorator(func):
    # func = the original function that we want to decorate

    def wrapper(*args, **kwargs):
        # wrapper = new function that adds extra behavior
        # *args  -> positional arguments
        # **kwargs -> keyword arguments

        # ----------------------------------------------------
        # BEFORE
        # Put extra work here that should happen BEFORE
        # the original function runs.
        # ----------------------------------------------------

        # Call the original function
        result = func(*args, **kwargs)

        # ----------------------------------------------------
        # AFTER
        # Put extra work here that should happen AFTER
        # the original function runs.
        # ----------------------------------------------------

        # Return the original function's result
        return result

    # Return wrapper so the original function is replaced
    # by the decorated version.
    return wrapper


# @my_decorator means:
#
# my_function = my_decorator(my_function)
#
# So whenever my_function() is called,
# the wrapper() function actually runs.


@my_decorator
def my_function():
    print("Decorator basic template")


my_function()