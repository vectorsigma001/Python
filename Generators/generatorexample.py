"""
Generators in Python provide a way to create iterators in a more memory-efficient manner. 
They allow you to iterate over data without loading the 
entire dataset into memory at once. Generators are defined using functions
and the yield statement.
"""

# ===================A simple generator function that yields numbers from 1 to 5:==================
def simple_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# Using the generator
gen = simple_generator()
for value in gen:
    print(value)

"""
1
2
3
4
5
"""

# =========Generator for Fibonacci Sequence=============
# A generator function to produce an infinite sequence of Fibonacci numbers:
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator
fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))


"""
0
1
1
2
3
5
8
13
21
34
"""

# ==============Generator with yield in a Loop===========
# A generator that yields squares of numbers up to a given number n:
def squares(n):
    for i in range(n):
        yield i * i

# Using the generator
squares_gen = squares(5)
for value in squares_gen:
    print(value)

"""
0
1
4
9
16
"""


# ===============Generator Expression ======================
# Similar to list comprehensions but for generators:
# List comprehension
squares_list = [x * x for x in range(5)]
print(squares_list)

# Generator expression
squares_gen = (x * x for x in range(5))
for value in squares_gen:
    print(value)

"""
[0, 1, 4, 9, 16]
0
1
4
9
16
"""


# =============Using Generators for File Processing ==============
# Generators are especially useful for processing large files
# where loading the entire file into memory is impractical:
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Using the generator
file_gen = read_large_file('large_file.txt')
for line in file_gen:
    print(line)


# ===========Generator with yield from =================
# The yield from statement is used to delegate part of a 
# generator’s operations to another generator:
def generator1():
    yield from range(5)

def generator2():
    yield from generator1()
    yield from range(5, 10)

# Using the generator
gen = generator2()
for value in gen:
    print(value)

"""
0
1
2
3
4
5
6
7
8
9
"""



# =============Generator for Prime Numbers =====================
# A more complex example, generating an infinite sequence of prime numbers:
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Using the generator
prime_gen = prime_generator()
for _ in range(10):
    print(next(prime_gen))

"""
2
3
5
7
11
13
17
19
23
29
"""
