# ================BASIC EXCEPTION HANDLING==============
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Error: Division by zero is not allowed.



# ================HANDLING MULTIPLE EXCPETION============
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid value.")

# Error: Division by zero is not allowed.


# ================Catching All Exceptions=============
try:
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")

# An error occurred: division by zero



# ==============Else Clause ==========================
# The else clause is executed if no exceptions are raised in the try block.
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"Result: {result}")

# Result: 5.0


# ============Finally Clause ===========================
# The finally clause is executed regardless of whether an exception is raised or not.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("This will always execute.")

"""
Error: Division by zero is not allowed.
This will always execute.
"""


# ==============Raising Exceptions===========================
# You can raise exceptions using the raise statement.
try:
    raise ValueError("A custom error message")
except ValueError as e:
    print(f"Caught an error: {e}")

# Caught an error: A custom error message


# =============Custom Exceptions==========================
# You can define your own exception classes by inheriting from the base Exception class.
class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise MyCustomError("This is a custom error")
except MyCustomError as e:
    print(f"Caught a custom error: {e.message}")

# Caught a custom error: This is a custom error


# =========Nested Try-Except Blocks======================
try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Inner error: Division by zero.")
        raise
except ZeroDivisionError:
    print("Outer error: Division by zero.")
"""
Inner error: Division by zero.
Outer error: Division by zero.
"""


# ========USING ASSERTION=====================
# Assertions can be used to set conditions that must be met in the code.
# If the condition is False, an AssertionError is raised.
try:
    x = 10
    assert x > 0, "x must be positive"
    assert x == 5, "x must be equal to 5"
except AssertionError as e:
    print(f"Assertion error: {e}")

# Assertion error: x must be equal to 5

# ========EXCEPTION HANDLING====================
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

result = divide(10, 0)
print(result)

# Cannot divide by zero
