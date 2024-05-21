"""
namedtuple is a factory function for creating tuple subclasses with named fields.
It makes tuples more readable by accessing elements using names instead of indices.
"""

from collections import namedtuple

# Example usage
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

print(p)
print(p.x, p.y)
print(p[0], p[1])

"""
Point(x=10, y=20)
10 20
10 20
"""
