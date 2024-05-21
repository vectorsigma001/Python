"""
These classes act as wrappers around dictionary, list, and string objects, 
making it easier to create custom dictionary, list, and string subclasses.
"""

from collections import UserDict, UserList, UserString

# Example usage of UserDict
class MyDict(UserDict):
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Keys must be strings")
        super().__setitem__(key, value)

my_dict = MyDict()
my_dict['a'] = 1
print(my_dict)

# Example usage of UserList
class MyList(UserList):
    def append(self, item):
        if not isinstance(item, int):
            raise TypeError("Items must be integers")
        super().append(item)

my_list = MyList([1, 2, 3])
my_list.append(4)
print(my_list)

# Example usage of UserString
class MyString(UserString):
    def append(self, string):
        self.data += string

my_string = MyString("Hello")
my_string.append(" World")
print(my_string)

"""
{'a': 1}
[1, 2, 3, 4]
Hello World
"""
