#==================1 REFERENCE TIMING===============
"""
Python uses reference counting to keep track of the number 
of references to each object in memory. When the reference 
count of an object drops to zero, the memory is deallocated.
"""
import sys

a = []      # Create an empty list
b = a       # b references the same list as a

print(sys.getrefcount(a))  # Output the reference count of the list
# Output: 3 (a, b, and the argument to getrefcount)

del a       # Remove the reference to the list
print(sys.getrefcount(b))  # Output the reference count of the list
# Output: 2 (b and the argument to getrefcount)

del b       # Remove the reference to the list
# Now the list has no references and will be deallocated


#=================2 GARBAGE COLLECTION ================
"""
Python uses a garbage collector to find and reclaim cycles of unreachable objects.
This complements the reference counting mechanism.
"""
import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create a cycle: n1 -> n2 -> n3 -> n1
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3
n3.next = n1

# Now, n1, n2, and n3 are part of a cycle and are unreachable
del n1
del n2
del n3

# Force a garbage collection to reclaim the memory
gc.collect()



# ===============3 Object Pools ==================
"""
Python maintains pools of small objects (like integers and short strings) 
to optimize memory allocation and deallocation. This is known as "interning."
"""
a = 256
b = 256

print(a is b)  # Output: True (because small integers are interned)

x = 257
y = 257

print(x is y)  # Output: False (because larger integers are not interned by default)


# ==================4 Memory Views =====================
"""
Memory views allow you to access the memory of another object
without creating a copy. This is useful for handling large data sets.
"""
import array

# Create an array of integers
arr = array.array('i', range(10))

# Create a memory view of the array
mem_view = memoryview(arr)

# Modify the memory view
mem_view[0] = 100

# The original array is also modified
print(arr[0])  # Output: 100

# ================5 Manual Memory Management (Using ctypes or numpy) ==================
"""
In some cases, you may need to manage memory manually using
libraries like ctypes or numpy.
"""
import ctypes

# Allocate memory for an integer
int_ptr = ctypes.pointer(ctypes.c_int(42))

# Access and modify the value
print(int_ptr.contents.value)  # Output: 42
int_ptr.contents.value = 100
print(int_ptr.contents.value)  # Output: 100

# Free the memory
ctypes.free(int_ptr)


#=================6 Example with numpy ==============================
import numpy as np

# Create a large array
arr = np.arange(1000000)

# Create a view of the array
view = arr[:100]

# Modify the view
view[0] = 999

# The original array is also modified
print(arr[0])  # Output: 999


