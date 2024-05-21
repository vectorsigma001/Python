"""
defaultdict is a dictionary subclass that provides default values for missing keys.
It is initialized with a default factory function.
"""

from collections import defaultdict

# Example usage
default_dict = defaultdict(int)
default_dict['apple'] += 1
default_dict['banana'] += 2

print(default_dict)
print(default_dict['orange'])  # Accessing a missing key

"""
defaultdict(<class 'int'>, {'apple': 1, 'banana': 2, 'orange': 0})
0
"""
