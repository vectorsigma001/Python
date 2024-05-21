"""
OrderedDict is a dictionary subclass that maintains the order of keys as they are inserted. 
It's useful when the order of items is important.
"""

from collections import OrderedDict

# Example usage
ordered_dict = OrderedDict()
ordered_dict['banana'] = 1
ordered_dict['apple'] = 2
ordered_dict['orange'] = 3

print(ordered_dict)
for key, value in ordered_dict.items():
    print(key, value)


"""
OrderedDict([('banana', 1), ('apple', 2), ('orange', 3)])
banana 1
apple 2
orange 3
"""
