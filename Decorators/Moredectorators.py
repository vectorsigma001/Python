#============basic class dectorators=========

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Something is happening before the function is called.")
        self.func(*args, **kwargs)
        print("Something is happening after the function is called.")

@MyDecorator
def say_hello():
    print("Hello!")

say_hello()

"""
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
"""


#=================Decorating Methods in a Class==============
def method_decorator(method):
    def wrapper(self, *args, **kwargs):
        print(f"Before {method.__name__}")
        result = method(self, *args, **kwargs)
        print(f"After {method.__name__}")
        return result
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello from method!")

obj = MyClass()
obj.say_hello()


"""
Before say_hello
Hello from method!
After say_hello
"""



#=============Class Method and Static Method Decorators===========
# Using @classmethod and @staticmethod:
class MyClass:
    @classmethod
    def class_method(cls):
        print(f"Class method called. Class is {cls}")

    @staticmethod
    def static_method():
        print("Static method called.")

obj = MyClass()
obj.class_method()
obj.static_method()

MyClass.class_method()
MyClass.static_method()

"""
Class method called. Class is <class '__main__.MyClass'>
Static method called.
Class method called. Class is <class '__main__.MyClass'>
Static method called.
"""

#=======================Property Decorators====================
# Using @property, @<property>.setter, and @<property>.deleter:
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value cannot be negative")
        self._value = new_value

    @value.deleter
    def value(self):
        del self._value

obj = MyClass(10)
print(obj.value)  # Calls the getter

obj.value = 20   # Calls the setter
print(obj.value)

del obj.value    # Calls the deleter

"""
10
20
(Note: The del obj.value line doesn't produce any visible output but deletes the value.)
"""




# ============= Nested Decorators ===================
# using multiple decorators
def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator One")
        return func(*args, **kwargs)
    return wrapper

def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator Two")
        return func(*args, **kwargs)
    return wrapper

@decorator_one
@decorator_two
def say_hello():
    print("Hello!")

say_hello()

"""
Decorator One
Decorator Two
Hello!
"""

