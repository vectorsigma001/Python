"""
Metaclasses in Python are a powerful tool for customizing class creation. 
A metaclass is a class whose instances are classes themselves. 
In other words, a metaclass defines the behavior of classes and can be used to 
modify how classes are constructed. Here are several examples to illustrate different aspects of metaclasses:
"""

# 1 ======================Basics Metaclass=============
# A simple example of using a metaclass to print a message when a class is created.
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass

# Output: Creating class MyClass


# 2 ======================Customizing Class Creation ===============
# Modifying class attributes during creation using a metaclass.
class AttributeAdderMeta(type):
    def __new__(cls, name, bases, dct):
        dct['added_attr'] = 'This is an added attribute'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=AttributeAdderMeta):
    pass

obj = MyClass()
print(obj.added_attr)  # Output: This is an added attribute

# 3 =======================Enforcing Class Constraints
# Using a metaclass to enforce certain constraints on the class definition.
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    def __init__(self):
        print("Singleton instance created")

# Test Singleton behavior
obj1 = SingletonClass()  # Output: Singleton instance created
obj2 = SingletonClass()
print(obj1 is obj2)  # Output: True


# 4 =====================Validating Class Attributes================
# A metaclass to ensure certain attributes are present in the class definition.
class ValidateAttributesMeta(type):
    def __new__(cls, name, bases, dct):
        if 'required_attr' not in dct:
            raise TypeError(f"{name} must define 'required_attr'")
        return super().__new__(cls, name, bases, dct)

class ValidClass(metaclass=ValidateAttributesMeta):
    required_attr = "This is required"

# This will raise an error
try:
    class InvalidClass(metaclass=ValidateAttributesMeta):
        pass
except TypeError as e:
    print(e)  # Output: InvalidClass must define 'required_attr'

# 5 =======================Dynamic Class Modification================
# Modifying methods dynamically during class creation.
class MethodAdderMeta(type):
    def __new__(cls, name, bases, dct):
        def new_method(self):
            return "This is a dynamically added method"
        dct['new_method'] = new_method
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MethodAdderMeta):
    pass

obj = MyClass()
print(obj.new_method())  # Output: This is a dynamically added method


# 6 ======================Inheriting from a Metaclass==========================
# Creating a metaclass that inherits from another metaclass.
class BaseMeta(type):
    def __new__(cls, name, bases, dct):
        dct['base_attr'] = "This is from BaseMeta"
        return super().__new__(cls, name, bases, dct)

class ChildMeta(BaseMeta):
    def __new__(cls, name, bases, dct):
        dct['child_attr'] = "This is from ChildMeta"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=ChildMeta):
    pass

obj = MyClass()
print(obj.base_attr)   # Output: This is from BaseMeta
print(obj.child_attr)  # Output: This is from ChildMeta

# 7 ======================Combining Metaclasses with Inheritance================
# Combining multiple metaclasses using abc.ABCMeta.
import abc

class CustomMeta(abc.ABCMeta):
    def __new__(cls, name, bases, dct):
        dct['custom_attr'] = "This is from CustomMeta"
        return super().__new__(cls, name, bases, dct)

class MyBaseClass(metaclass=CustomMeta):
    pass

class MyClass(MyBaseClass):
    pass

obj = MyClass()
print(obj.custom_attr)  # Output: This is from CustomMeta

"""
These examples demonstrate the versatility and power of metaclasses in Python.
They can be used for a wide range of purposes, from enforcing constraints and
adding attributes or methods to creating singletons and modifying inheritance behavior.
"""
