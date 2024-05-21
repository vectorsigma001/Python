# Magic methods (also known as dunder methods,
# because they have double underscores at the beginning 
# and end of their names) are special methods in Python that allow you to 
# define how objects of your classes behave with built-in Python operations. 
# Here's an overview of some common magic methods with examples.


#===============Example Class Using Magic Methods==================
# Let's create a class Vector to demonstrate various magic methods.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __repr__ for an official string representation of the object
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # __str__ for a user-friendly string representation of the object
    def __str__(self):
        return f"({self.x}, {self.y})"

    # __add__ for addition
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    # __sub__ for subtraction
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    # __mul__ for scalar multiplication
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    # __eq__ for equality check
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    # __len__ to provide the magnitude of the vector as its "length"
    def __len__(self):
        return int((self.x**2 + self.y**2) ** 0.5)

    # __getitem__ and __setitem__ for indexing
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Index out of range")


# Creating Vector instances
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# __repr__ and __str__
print(repr(v1))  # Output: Vector(2, 3)
print(str(v1))   # Output: (2, 3)

# __add__
v3 = v1 + v2
print(v3)  # Output: (6, 8)

# __sub__
v4 = v1 - v2
print(v4)  # Output: (-2, -2)

# __mul__
v5 = v1 * 3
print(v5)  # Output: (6, 9)

# __eq__
print(v1 == v2)  # Output: False
print(v1 == Vector(2, 3))  # Output: True

# __len__
print(len(v1))  # Output: 3 (magnitude of Vector(2, 3) is approximately 3.605)

# __getitem__ and __setitem__
print(v1[0])  # Output: 2
print(v1[1])  # Output: 3

v1[0] = 10
v1[1] = 20
print(v1)  # Output: (10, 20)


"""
#=============Explanation of Magic Methods==========

__init__(self, x, y): 
Constructor method for initializing the Vector object with x and y coordinates.

__repr__(self):
Provides the "official" string representation of the Vector object, useful for debugging.

__str__(self):
Provides a user-friendly string representation of the Vector object, used by the print function.

__add__(self, other): 
Defines the behavior of the addition operator (+) for Vector objects.

__sub__(self, other):
Defines the behavior of the subtraction operator (-) for Vector objects.

__mul__(self, scalar):
Defines the behavior of the multiplication operator (*) for Vector objects when multiplied by a scalar

__eq__(self, other):
Defines the behavior of the equality operator (==) for Vector objects.

__len__(self): 
Provides the "length" of the Vector object, interpreted as the magnitude of the vector.

__getitem__(self, index):
Allows indexing to get the x and y coordinates.

__setitem__(self, index, value): 
Allows indexing to set the x and y coordinates.

These magic methods make the Vector class behave more like a built-in Python type, allowing for more intuitive and readable code.
"""
