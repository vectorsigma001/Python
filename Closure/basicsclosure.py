# 1===================Basic Closure ===================
def outer_function(msg):
    message = msg
    
    def inner_function():
        print(message)
    
    return inner_function

# Create a closure
closure = outer_function("Hello, World!")

# Call the closure
closure()  # Output: Hello, World!


# 2 ==============Using Closures for State=======================
"""
Closures are useful for maintaining state. Here's an example of a closure that maintains a count:
"""
def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

# Create two independent counters
counter1 = make_counter()
counter2 = make_counter()

print(counter1())  # Output: 1
print(counter1())  # Output: 2

print(counter2())  # Output: 1
print(counter2())  # Output: 2

"""
In this example, make_counter defines a count variable and an inner function counter
that increments and returns count. The nonlocal keyword is used to indicate that count 
is not a local variable of counter, but is defined in the enclosing scope of make_counter.
Each time make_counter is called, a new count variable is created, allowing for independent counters.
"""


# 3 ==================Using Closures to Configure Functions ====================
""" Closures can also be used to create functions with configurable behavior: """
def power(exponent):
    def power_of(base):
        return base ** exponent
    return power_of

# Create functions to square and cube numbers
square = power(2)
cube = power(3)

print(square(2))  # Output: 4
print(square(3))  # Output: 9

print(cube(2))    # Output: 8
print(cube(3))    # Output: 27

"""
Closures are a powerful feature in Python,
allowing for more modular, maintainable, and 
elegant code by capturing and maintaining state without the need for global variables.
"""


