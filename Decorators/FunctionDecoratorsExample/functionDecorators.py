# ==============PROGRAM NUMBER ONE ==========================
# BASIC FUNCTION DECORATOR
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

"""
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
"""

# DECORATORS WITH ARGUMENTS
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")
"""
Hello Alice
Hello Alice
Hello Alice
"""

# Decorator with functools.wraps:
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
"""
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
"""
