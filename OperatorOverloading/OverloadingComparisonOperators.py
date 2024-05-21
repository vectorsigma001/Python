# In addition to __eq__, you can overload other comparison operators like __ne__ (not equal),
# __lt__ (less than), __le__ (less than or equal to), __gt__ (greater than), 
# and __ge__ (greater than or equal to).

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) <= (other.x**2 + other.y**2)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) > (other.x**2 + other.y**2)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) >= (other.x**2 + other.y**2)
        return NotImplemented

# Using the Vector class
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Equality and inequality
print(v1 == v2)  # Output: False
print(v1 != v2)  # Output: True

# Less than and less than or equal to
print(v1 < v2)  # Output: True
print(v1 <= v2)  # Output: True

# Greater than and greater than or equal to
print(v1 > v2)  # Output: False
print(v1 >= v2)  # Output: False
