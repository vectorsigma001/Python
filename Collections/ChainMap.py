"""
ChainMap groups multiple dictionaries into a single view. 
It's useful for combining multiple dictionaries or scopes.
"""

from collections import ChainMap

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain_map = ChainMap(dict1, dict2)

print(chain_map)
print(chain_map['a'])
print(chain_map['b'])  # From dict1, the first map in the chain
print(chain_map['c'])  # From dict2, the second map in the chain

"""
ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
1
2
4
"""
