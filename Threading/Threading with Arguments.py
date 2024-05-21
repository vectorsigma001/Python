# Passing arguments to the target function of a thread:
import threading
import time

def print_numbers(prefix, count):
    for i in range(1, count + 1):
        time.sleep(1)
        print(f"{prefix} Number: {i}")

# Create a thread with arguments
thread = threading.Thread(target=print_numbers, args=("Thread-1", 5))

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()

print("Thread has finished execution.")

"""
Thread-1 Number: 1
Thread-1 Number: 2
Thread-1 Number: 3
Thread-1 Number: 4
Thread-1 Number: 5
Thread has finished execution.
"""
