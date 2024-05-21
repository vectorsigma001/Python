# You can also overload arithmetic operators 
# like __truediv__ (true division), __floordiv__ (floor division),
# __mod__ (modulus), and __pow__ (exponentiation).

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented

    def __floordiv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x // scalar, self.y // scalar)
        return NotImplemented

    def __mod__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x % scalar, self.y % scalar)
        return NotImplemented

    def __pow__(self, exponent):
        if isinstance(exponent, (int, float)):
            return Vector(self.x ** exponent, self.y ** exponent)
        return NotImplemented

# Using the Vector class
v1 = Vector(6, 8)

# True division
v2 = v1 / 2
print(v2)  # Output: (3.0, 4.0)

# Floor division
v3 = v1 // 2
print(v3)  # Output: (3, 4)

# Modulus
v4 = v1 % 5
print(v4)  # Output: (1, 3)

# Exponentiation
v5 = v1 ** 2
print(v5)  # Output: (36, 64)


