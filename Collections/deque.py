"""
deque (double-ended queue) is a list-like container 
with fast appends and pops from both ends. 
It's useful for implementing queues and stacks.
"""

from collections import deque

# Example usage
d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
print(d)

d.pop()
d.popleft()
print(d)

"""
deque([0, 1, 2, 3, 4])
deque([1, 2, 3])
"""
