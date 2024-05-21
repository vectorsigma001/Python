"""
Counter is a dictionary subclass for counting hashable objects.
It's useful for counting occurrences of items in an iterable.
"""
from collections import Counter

# Example usage
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_count = Counter(words)

print(word_count)
print(word_count['apple'])  # Count of 'apple'
print(word_count.most_common(2))  # Two most common elements
"""
Counter({'apple': 3, 'banana': 2, 'orange': 1})
3
[('apple', 3), ('banana', 2)]

"""
