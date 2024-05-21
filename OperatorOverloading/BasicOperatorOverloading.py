# Let's create a Vector class and overload some basic operators.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    # Addition
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    # Subtraction
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    # Multiplication with a scalar
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    # Equality check
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    # Less than
    def __lt__(self, other):
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
        return NotImplemented

    # Greater than
    def __gt__(self, other):
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) > (other.x**2 + other.y**2)
        return NotImplemented

# Using the Vector class
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Addition
v3 = v1 + v2
print(v3)  # Output: (6, 8)

# Subtraction
v4 = v1 - v2
print(v4)  # Output: (-2, -2)

# Multiplication with a scalar
v5 = v1 * 3
print(v5)  # Output: (6, 9)

# Equality check
print(v1 == v2)  # Output: False
print(v1 == Vector(2, 3))  # Output: True

# Less than and greater than
print(v1 < v2)  # Output: True
print(v1 > v2)  # Output: False
